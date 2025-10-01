#!/usr/bin/env python3
"""
generate_hr_intent_dataset.py

Generate synthetic HR chatbot training data using GPT-4o-mini with function calling.

Output:
    - Single CSV with columns: query, intent
    - One row per synthetic utterance

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
EXAMPLES_PER_INTENT = 300
BATCH_SIZE = 50
MAX_RETRIES = 3
SLEEP_BETWEEN_RETRIES = 2.0

OUTPUT_FILE = Path("hr_intents_dataset.csv")

INTENTS = [
    "leave_balance",
    "policy_query",
    "headcount_report",
    "holiday_calendar",
    "payslip_request",
    "tax_documents",
    "benefits_query",
    "exit_process",
    "human_handoff",
    "profile_information_request",
    "project_Information"
]

# -------------------------
# FUNCTION SCHEMA
# -------------------------
FUNCTION_SCHEMA = {
    "name": "return_examples",
    "description": "Return a set of user queries for HR chatbot intents",
    "parameters": {
        "type": "object",
        "properties": {
            "examples": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "intent": {"type": "string"}
                    },
                    "required": ["query", "intent"]
                }
            }
        },
        "required": ["examples"]
    }
}

# -------------------------
# GENERATION
# -------------------------
def call_gpt(intent: str, n: int):
    """Generate n examples for a given intent using GPT function calling."""
    user_prompt = (
        f"Generate {n} distinct user queries for an HR chatbot. "
        f"All queries must be read-only retrieval (no updates or modifications). "
        f"The intent for all queries is '{intent}'. "
        f"Return structured JSON using the function schema."
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You generate HR chatbot training queries."},
                    {"role": "user", "content": user_prompt}
                ],
                functions=[FUNCTION_SCHEMA],
                function_call={"name": "return_examples"},
                temperature=0.3,
                max_tokens=1500,
            )

            args_text = resp.choices[0].message.function_call.arguments
            data = json.loads(args_text)
            return data.get("examples", [])
        except Exception as e:
            if attempt == MAX_RETRIES:
                print(f"[ERROR] Giving up on {intent}: {e}")
                return []
            time.sleep(SLEEP_BETWEEN_RETRIES * attempt)
    return []


def generate_dataset():
    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["query", "intent"])  # header

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
                    query = ex.get("query", "").strip()
                    if not query:
                        continue
                    writer.writerow([query, intent])
                    count += 1
                    pbar.update(1)
            print(f"Intent '{intent}': {count}/{EXAMPLES_PER_INTENT} examples done.")
        pbar.close()
    print(f"\n✅ Dataset saved to {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    print("This script will generate HR chatbot dataset using gpt-4o-mini.")
    proceed = input("Proceed? (y/n): ").strip().lower()
    if proceed != "y":
        raise SystemExit("Aborted.")
    generate_dataset()
