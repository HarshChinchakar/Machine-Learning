LawGPT Model
This repository provides a comprehensive overview of the LawGPT model implementation, focusing on legal document analysis using the MiniLM-L6-v2 architecture. The model is designed for efficiency, offering a constant response time of 2 seconds, despite being trained on limited datasets.

Table of Contents
Introduction
Installation
Code Explanation
Step 1: Install Dependencies
Step 2: Import Libraries
Step 3: Mount Google Drive
Step 4: Load Model and Tokenizer
Step 5: Define Helper Functions
Step 6: Process PDF and Perform Inference
Performance Metrics
Limitations
Conclusion
Introduction
The LawGPT model is tailored for classifying legal documents, utilizing the MiniLM-L6-v2 architecture from the transformers library. It is optimized for real-time applications with a consistent response time of 2 seconds.

Installation
To set up the environment for running the LawGPT model, follow these steps:

Step 1: Install Dependencies
Install the necessary libraries using the following command:

bash
Copy code
pip install transformers PyPDF2
transformers: For the model and tokenizer.
PyPDF2: For handling PDF files.
Step 2: Upload .pkl Files
Before running the model, make sure to upload the required .pkl files that contain the model's weights and configurations.

Step 3: Import Libraries
Import the necessary modules:

python
Copy code
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from PyPDF2 import PdfReader
Step 4: Mount Google Drive
To access files stored in Google Drive, use:

python
Copy code
from google.colab import drive
drive.mount('/content/drive')
This will allow you to load datasets and models stored in the cloud.

Code Explanation
Step 1: Install Dependencies
Install essential libraries using pip:

transformers: Provides tools for NLP.
PyPDF2: Used for extracting text from PDF files.
Step 2: Import Libraries
Import required modules from the installed libraries:

AutoTokenizer and AutoModelForSequenceClassification from transformers.
PdfReader from PyPDF2.
Step 3: Mount Google Drive
Mounting Google Drive gives access to datasets and models stored in the cloud.

Step 4: Load Model and Tokenizer
Initialize the tokenizer and model:

python
Copy code
tokenizer = AutoTokenizer.from_pretrained("microsoft/MiniLM-L6-v2")
model = AutoModelForSequenceClassification.from_pretrained("microsoft/MiniLM-L6-v2")
Step 5: Define Helper Functions
Create functions to preprocess data, perform inference, and post-process the results.

Step 6: Process PDF and Perform Inference
Read a PDF, extract its content, and classify the text using the loaded model.

Performance Metrics
The LawGPT model achieves a consistent response time of 2 seconds per query, ensuring efficient processing of legal documents.

Limitations
Datasets: The model has been trained and validated on a limited dataset, which may affect its generalizability.
Scope: It is specifically designed for legal document classification and may not perform optimally with other types of text.
Conclusion
LawGPT leverages the MiniLM-L6-v2 architecture to provide fast and efficient legal document analysis. Future improvements could include expanding the dataset and refining the model's capabilities.

Credits
Developed by Harsh Chinchakar under DeepCytes 2024. For questions or contributions, feel free to reach out. - harshchinchakar33@gmail.com
All Credits and ownership stays with Harsh Chinchakar. 
