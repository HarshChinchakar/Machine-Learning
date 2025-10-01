# HR Chatbot Data Generation Scripts

## Overview

This repository contains scripts to generate **synthetic HR chatbot training data** using **GPT-4o-mini**. The purpose is to create large-scale datasets for fine-tuning intent, task, slot, and role classifiers for HR-related queries.  

There are **two main scripts**:

1. **`generate_hr_intent_dataset.py`**  
   - Generates a dataset with **`query` and `intent`** only.  
   - Suitable for single-head models predicting intent and task.  
   - Each intent generates multiple synthetic queries for training.  

2. **`generate_hr_intent_dataset_enhanced.py`**  
   - Generates a dataset with **`text`, `intent`, `task`, `slots`, and `role`**.  
   - Suitable for **multi-head models** predicting intent, task, slots, and role.  
   - Includes realistic placeholders, minor noise, and indirect phrasings for robust model training.

Both scripts use **function calling** with GPT-4o-mini to produce structured JSON outputs that can be directly saved to CSV.

---

## Repository Structure

├── Dataset/ # Generated datasets (CSV files)  
│ ├── hr_intents_dataset.csv # Intent + query dataset  
│ └── hr_intents_dataset_expanded.csv # Intent + task + slots + role dataset  
├── scripts/ # Python scripts for data generation  
│ ├── generate_hr_intent_dataset.py  
│ └── generate_hr_intent_dataset_enhanced.py  
├── .env # Environment file with OPENAI_API_KEY (ignored in Git)  
└── README.md # Documentation    

---

## Script Details
1. generate_hr_intent_dataset.py  
# Generates intent-focused dataset with columns:  **query, intent**   
# Configurable parameters:  
**EXAMPLES_PER_INTENT** – number of queries per intent.  
**BATCH_SIZE** – number of queries generated per API call.  
**MODEL** – GPT model used (gpt-4o-mini).  
Handles retrying failed API calls and uses progress bars for monitoring.  

---

## generate_hr_intent_dataset_enhanced.py  
# Generates multi-head dataset with columns:  
**text, intent, task, slots, role**    
Adds structured slots for each query with placeholder values.  
Role can be employee or hr.  
Task mapping and test case coverage ensure robust and realistic data generation.  
Configurable parameters are similar to the simpler script.  

---

## Notes
Synthetic data is generated programmatically; avoid real PII.  
The enhanced script is suitable for multi-task learning (intent + task + slot + role).  
Datasets are saved as CSV files in the Dataset/ folder.  
For large-scale datasets, consider batching API calls and monitoring usage.  

---

## Authors
Harsh Chinchakar – Development of data generation scripts and pipeline
