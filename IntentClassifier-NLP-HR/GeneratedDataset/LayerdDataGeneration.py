#!/usr/bin/env python3
"""
generate_hr_intent_dataset_enhanced.py

Generate high-quality synthetic HR chatbot training data using GPT-4o-mini with function calling.

Output:
    - Single CSV with columns: text, intent, task, slots, role

Requirements:
    pip install openai tqdm python-dotenv
"""

import os
import json
import time
import csv
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------
# ENV + CLIENT
# -------------------------
load_dotenv("/home/harshchinchakar/WORK Files/TataPlay/Finetuned Model/Dataset/.env")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("Missing OPENAI_API_KEY in .env file")
client = OpenAI(api_key=api_key)

# -------------------------
# CONFIG
# -------------------------
MODEL = "gpt-4o-mini"
EXAMPLES_PER_INTENT = 600
BATCH_SIZE = 50
MAX_RETRIES = 4
SLEEP_BETWEEN_RETRIES = 2.0
OUTPUT_FILE = Path("hr_intents_dataset_expanded.csv")

INTENTS = [
    "leave_balance", "policy_query", "headcount_report", "holiday_calendar",
    "payslip_request", "tax_documents", "benefits_query", "exit_process",
    "human_handoff", "profile_information_request", "project_information"
]

TASKS_BY_INTENT = {
    "profile_information_request": "profile_phone, profile_email, profile_address, profile_manager, profile_designation",
    "leave_balance": "leave_balance_summary, leave_balance_by_type, leave_history, upcoming_approved_leaves",
    "policy_query": "policy_travel, policy_reimbursement, policy_leave",
    "headcount_report": "headcount_by_department, headcount_by_location, headcount_by_role",
    "holiday_calendar": "holiday_list_year, holiday_next",
    "payslip_request": "payslip_month, payslip_latest",
    "tax_documents": "tax_document_year, tax_form_latest",
    "benefits_query": "benefits_perks, benefits_insurance",
    "exit_process": "exit_process_steps, exit_final_settlement",
    "human_handoff": "human_escalation_request",
    "project_information": "project_status, project_deadline, project_owner"
}

TC_SUMMARY = [
    "TC01: ask for registered address", "TC02: ask for emergency contact",
    "TC03: ask when contact info last updated", "TC04: ask for registered email",
    "TC05: ask for unavailable field -> expect error", "TC06: visibility/formatting of returned data",
    "TC07-13: leave balance, type-specific, history, upcoming",
    "TC11-13: HR queries for other employees (HR role only)",
    "TC14-21: headcount reports and export", "TC19-25: leave reports, filters, exports",
    "TC26-31: performance / timings", "TC31-35: security, access controls, logging",
    "TC36-42: availability, maintenance, error handling"
]

FUNCTION_SCHEMA = {
    "name": "return_examples",
    "description": "Return a set of example user queries for HR chatbot training",
    "parameters": {
        "type": "object",
        "properties": {
            "examples": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "intent": {"type": "string"},
                        "task": {"type": "string"},
                        "slots": {"type": "object"},
                        "role": {"type": "string", "enum": ["employee", "hr"]}
                    },
                    "required": ["text", "intent", "task", "slots", "role"]
                }
            }
        },
        "required": ["examples"]
    }
}

SYSTEM_PROMPT = (
    "You are a strict data-generation assistant. Produce realistic, concise user queries that an HR chatbot would receive. "
    "All queries MUST be read-only (retrieval) — do NOT request or suggest any data creation, update, or deletion. "
    "Consider all User Types and have different write styles, also write indirect queries which will make the model robust. "
    "Avoid using real PII. Use placeholders if necessary. Include subtle noise and indirect phrasings to improve robustness. "
    "All returned objects MUST include the 'slots' field with realistic values where applicable. "
    "If a query refers to a parameter (like 'month', 'year', 'leave_type', etc.), populate it with a placeholder value "
    "(e.g., 'August' for month, '2025' for year, 'vacation' for leave_type). "
    "Return results only via the function call 'return_examples' following the provided schema. Do not output plain text."
)

USER_PROMPT_TEMPLATE = (
    "Generate exactly {n} distinct examples for the canonical intent '{intent}'.\n"
    "Requirements:\n"
    " - Use the provided intent label exactly as '{intent}'.\n"
    " - Use a specific task label (choose the most specific applicable task) from this example list:\n"
    "   {task_list}\n"
    " - For 'slots', provide a JSON object with realistic placeholder values for every required slot relevant to the intent (assume slots of an enterprise) "
    "(e.g., {{\"month\":\"August\", \"year\":\"2025\", \"leave_type\":\"vacation\"}}). Do NOT leave slots empty.\n"
    " - Role must be either 'employee' or 'hr'. If the query targets another employee (HR only), set role='hr'.\n"
    " - Include minor noise / indirect phrasing (e.g., 'I think my email was...?', 'Where could I find my payslip for May?').\n"
    " - Keep each 'text' to 1-2 sentences max. No PII. No multi-turn dialogs.\n"
    " - Ensure coverage across scenarios: {tc_summary}\n"
    "Return exactly {n} objects as the 'examples' array and nothing else."
)

def _attempt_json_fix(s: str) -> str:
    s2 = s.strip().replace("\n", " ").replace("'", '"')
    s2 = s2.replace(",]", "]").replace(", }", " }")
    return s2

def _extract_examples(resp) -> list:
    try:
        args_text = resp.choices[0].message.function_call.arguments
        try:
            return json.loads(args_text).get("examples", [])
        except json.JSONDecodeError:
            return json.loads(_attempt_json_fix(args_text)).get("examples", [])
    except Exception:
        return []

def call_gpt(intent: str, n: int):
    task_list = TASKS_BY_INTENT.get(intent, "")
    tc_summary = "; ".join(TC_SUMMARY)
    user_prompt = USER_PROMPT_TEMPLATE.format(n=n, intent=intent, task_list=task_list, tc_summary=tc_summary)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                functions=[FUNCTION_SCHEMA],
                function_call={"name": "return_examples"},
                temperature=0.25,
                max_tokens=2000,
            )
            examples = _extract_examples(resp)
            return examples if isinstance(examples, list) else []
        except Exception as e:
            if attempt == MAX_RETRIES:
                print(f"[ERROR] Giving up on {intent}: {e}")
                return []
            time.sleep(SLEEP_BETWEEN_RETRIES * attempt)
    return []

def generate_dataset():
    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "intent", "task", "slots", "role"])
        seen_texts = set()
        total = EXAMPLES_PER_INTENT * len(INTENTS)
        pbar = tqdm(total=total, desc="Generating", unit="ex")

        for intent in INTENTS:
            count = 0
            while count < EXAMPLES_PER_INTENT:
                to_request = min(BATCH_SIZE, EXAMPLES_PER_INTENT - count)
                examples = call_gpt(intent, to_request)
                if not examples:
                    break
                for ex in examples:
                    text = ex.get("text", "").strip()
                    if not text or text.lower() in seen_texts:
                        continue
                    seen_texts.add(text.lower())
                    writer.writerow([
                        text,
                        ex.get("intent", intent),
                        ex.get("task", "unknown_task"),
                        json.dumps(ex.get("slots", {}), ensure_ascii=False),
                        ex.get("role", "employee")
                    ])
                    count += 1
                    pbar.update(1)
            print(f"Intent '{intent}': {count}/{EXAMPLES_PER_INTENT} examples done.")
        pbar.close()
    print(f"\n✅ Dataset saved to {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    print("This script will generate expanded HR chatbot dataset using gpt-4o-mini.")
    proceed = input("Proceed? (y/n): ").strip().lower()
    if proceed != "y":
        raise SystemExit("Aborted.")
    generate_dataset()
