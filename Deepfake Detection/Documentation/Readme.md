# LawGPT Model Documentation

## Overview
This repository provides a comprehensive overview of the LawGPT model implementation, focusing on legal document analysis using the MiniLM-L6-v2 architecture. The model is designed for efficiency, offering a constant response time of 2 seconds, despite being trained on limited datasets.

## Table of Contents
- [Overview](#overview)
- [Introduction](#introduction)
- [Installation](#installation)
  - [Step 1: Install Dependencies](#step-1-install-dependencies)
  - [Step 2: Upload .pkl Files](#step-2-upload-pkl-files)
  - [Step 3: Import Libraries](#step-3-import-libraries)
  - [Step 4: Mount Google Drive](#step-4-mount-google-drive)
- [Code Explanation](#code-explanation)
  - [Step 1: Install Dependencies](#step-1-install-dependencies-1)
  - [Step 2: Import Libraries](#step-2-import-libraries)
  - [Step 3: Mount Google Drive](#step-3-mount-google-drive)
  - [Step 4: Load Model and Tokenizer](#step-4-load-model-and-tokenizer)
  - [Step 5: Define Helper Functions](#step-5-define-helper-functions)
  - [Step 6: Process PDF and Perform Inference](#step-6-process-pdf-and-perform-inference)
- [Performance Metrics](#performance-metrics)
- [Limitations](#limitations)
- [Conclusion](#conclusion)
- [Credits](#credits)

## Introduction

The LawGPT model is tailored for classifying legal documents, utilizing the MiniLM-L6-v2 architecture from the transformers library. It is optimized for real-time applications with a consistent response time of 2 seconds.

## Installation

To set up the environment for running the LawGPT model, follow these steps:

### Step 1: Install Dependencies

Install the necessary libraries using the following command:

```bash
pip install transformers PyPDF2
```

- `transformers`: For the model and tokenizer.
- `PyPDF2`: For handling PDF files.

### Step 2: Upload .pkl Files

Before running the model, make sure to upload the required `.pkl` files that contain the model's weights and configurations.

### Step 3: Import Libraries

Import the necessary modules:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from PyPDF2 import PdfReader
```

### Step 4: Mount Google Drive

To access files stored in Google Drive, use:

```python
from google.colab import drive
drive.mount('/content/drive')
```

This will allow you to load datasets and models stored in the cloud.

## Code Explanation

### Step 1: Install Dependencies

Install essential libraries using pip:

- `transformers`: Provides tools for NLP.
- `PyPDF2`: Used for extracting text from PDF files.

### Step 2: Import Libraries

Import required modules from the installed libraries:

- `AutoTokenizer` and `AutoModelForSequenceClassification` from `transformers`.
- `PdfReader` from `PyPDF2`.

### Step 3: Mount Google Drive

Mounting Google Drive gives access to datasets and models stored in the cloud.

### Step 4: Load Model and Tokenizer

Initialize the tokenizer and model:

```python
tokenizer = AutoTokenizer.from_pretrained("microsoft/MiniLM-L6-v2")
model = AutoModelForSequenceClassification.from_pretrained("microsoft/MiniLM-L6-v2")
```

### Step 5: Define Helper Functions

Create functions to preprocess data, perform inference, and post-process the results.

### Step 6: Process PDF and Perform Inference

Read a PDF, extract its content, and classify the text using the loaded model.

## Performance Metrics

The LawGPT model achieves a consistent response time of 2 seconds per query, ensuring efficient processing of legal documents.

## Limitations

- **Datasets**: The model has been trained and validated on a limited dataset, which may affect its generalizability.
- **Scope**: It is specifically designed for legal document classification and may not perform optimally with other types of text.

## Conclusion

LawGPT leverages the MiniLM-L6-v2 architecture to provide fast and efficient legal document analysis. Future improvements could include expanding the dataset and refining the model's capabilities.

## Credits

Developed by Harsh Chinchakar under DeepCytes 2024. For questions or contributions, feel free to reach out: [harshchinchakar33@gmail.com](mailto:harshchinchakar33@gmail.com).

All credits and ownership stay with Harsh Chinchakar.

