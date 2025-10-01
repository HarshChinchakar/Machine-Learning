# Tataplay Intent Classifier

## Overview

This repository contains scripts and models for **intent classification** and **slot extraction** for HR-related queries. The project focuses on the following tasks:

1. **Data Cleaning & Preprocessing** – Preparing raw datasets for model training.  
2. **Data Generation** – Expanding and augmenting datasets for better model generalization.  
3. **Model Fine-Tuning** – Training transformer-based models to classify intents, tasks, and extract slot entities.  
4. **Inference** – Deploying trained models to predict intents, tasks, and slots for new queries.

The repository provides all scripts required for **training, fine-tuning, and inference**, along with model checkpoints and tokenizers.

---

## Repository Structure
├── Finetuned Model/ # Folder containing all trained and fine-tuned models
│ ├── MultiThreadModel/ # Multi-head classifier for HR intent, task, and slot prediction
│ └── finetuned_intent_model/ # Single-head classifier for intent prediction
├── Dataset/ # CSV files for training and testing
├── scripts/ # Python scripts for data processing, training, and inference
├── .gitignore # Git ignore rules for sensitive and large files
└── README.md # Project documentation


---

## Key Components

### 1. Fine-Tuning Script

The fine-tuning script trains a transformer-based model (`sentence-transformers/all-MiniLM-L6-v2`) for HR intent classification:

- Loads and preprocesses the training dataset (`CSV` format).  
- Encodes text using `AutoTokenizer` and creates a PyTorch `Dataset`.  
- Fine-tunes the model with a configurable number of epochs, batch size, learning rate, and gradient clipping.  
- Performs validation at the end of each epoch and prints **accuracy** and **weighted F1 score**.  
- Saves the fine-tuned model, tokenizer, and label mapping for later use.

**Libraries used:** `pandas`, `torch`, `transformers`, `sklearn`, `tqdm`.

---

### 2. Multi-Head Inference Script

The inference script loads the trained multi-head model to predict:

- **Intent** – The primary user intent.  
- **Task** – Related task categories.  
- **Slots** – Extracted entities from user queries (BIO tagging).  

Key features:

- Uses `AutoTokenizer` and a custom `MultiHeadClassifier`.  
- Loads pre-trained model weights (`.pt` files) and mapping JSON files (`intent_mapping.json`, `task_mapping.json`, `slot_label_list.json`).  
- Decodes predicted BIO slot sequences into a dictionary of slot-value pairs.  
- Runs inference on CPU or GPU.  
- Prints inference time for each query.

---
**Example usage:**

python inference.py
# Enter query (or 'quit'): I want to apply for leave tomorrow
# {'intent': 'LeaveRequest', 'task': 'ApplyLeave', 'slots': {'date': 'tomorrow'}, 'role': 'employee'}

---
Authors
Harsh Chinchakar – Development, fine-tuning, and inference scripts.
