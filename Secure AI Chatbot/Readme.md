# Secure AI Chatbot Documentation

## Flowchart Overview
The system consists of multiple layers that work together to process user inputs securely, generate appropriate responses, and ensure data privacy. Here is a detailed explanation of each component in the flow:

- AES - Adversarial Attack Check - NLP Context Classification - Content Filtering - LLM Guard - NLP Processing - Query Processing (LawGPT or General LLM) - Hosting

## Table of Contents
- [1. AES (Advanced Encryption Standard)](#1-aes-advanced-encryption-standard)
- [2. Adversarial Attack Check](#2-adversarial-attack-check)
- [3. NLP Context Classification](#3-nlp-context-classification)
- [4. Content Filtering](#4-content-filtering)
- [5. LLM Guard](#5-llm-guard)
- [6. NLP Processing](#6-nlp-processing)
- [7. Query Processing](#7-query-processing)
- [8. Hosting on Azure](#8-hosting-on-azure)
- [9. Standard Operating Procedures (SOP)](#9-standard-operating-procedures-sop)
- [Screenshots and Diagrams](#screenshots-and-diagrams)

## 1. AES (Advanced Encryption Standard)
**Purpose**: Encrypts the user input before sending it through the pipeline, ensuring data security during transit.

**Implementation**: Uses AES-256 for strong encryption. The data is encrypted at the beginning of the flow and decrypted once it reaches the processing layers.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Key and IV setup
key = b'YourAESKeyHere1234' # 16 bytes key
iv = b'YourAESIVHere123456' # 16 bytes IV

# Encryption
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(user_input.encode(), AES.block_size))

# Decryption when processing
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(decipher.decrypt(ciphertext), AES.block_size)
```

## 2. Adversarial Attack Check
**Purpose**: Uses ReBuff.AI or similar frameworks to identify and mitigate adversarial attacks in user input.

**Implementation**: Runs checks on the decrypted input to identify potentially malicious or adversarial patterns.

```python
import re
from rebuff import AdversarialChecker

# Initialize Adversarial Checker
checker = AdversarialChecker()

# Check for adversarial attacks
if checker.is_adversarial(decrypted_data):
    raise ValueError("Adversarial input detected")
```

## 3. NLP Context Classification
**Purpose**: Classifies the context of the input as either legal (1) or general (0), guiding the LLM Layer on which model to use for query processing.

**Implementation**: Uses NLP models to extract keywords and determine the context of the conversation.

```python
from nlp_module import ContextClassifier

# Initialize context classifier
classifier = ContextClassifier()

# Classify the context
context_type = classifier.classify_context(decrypted_data)
# context_type = 1 if legal, 0 if general
```

## 4. Content Filtering
**Purpose**: Filters out inappropriate or irrelevant content based on predefined rules and guidelines.

**Implementation**: Uses frameworks like LLM Guard to moderate and secure input.

```python
from llm_guard import ContentFilter

# Initialize content filter
content_filter = ContentFilter()

# Filter the input
filtered_content = content_filter.filter(decrypted_data)
if not filtered_content:
    raise ValueError("Content rejected by filter")
```

## 5. LLM Guard
**Purpose**: Serves as an additional layer of protection, ensuring that inputs to the LLM do not violate security or policy guidelines.

**Implementation**: Validates the input against advanced criteria and checks for any unauthorized content.

```python
from llm_guard import LLMGuard

# Initialize LLM Guard
llm_guard = LLMGuard()

# Guard validation
if not llm_guard.validate(filtered_content):
    raise ValueError("Input failed LLM Guard validation")
```

## 6. NLP Processing
**Purpose**: Processes validated content, including keyword extraction, sentiment analysis, and embedding generation.

**Implementation**: Extracts relevant data and prepares it for LLM processing.

```python
from nlp_module import NLPProcessor

# Initialize NLP Processor
nlp_processor = NLPProcessor()

# Extract keywords and other NLP elements
keywords, sentiment = nlp_processor.process(filtered_content)
```

## 7. Query Processing
**Purpose**: Directs the query to the appropriate model for response generation based on context classification.
- **If Legal Context (1)**: Uses LawGPT for specialized legal or cybersecurity queries.
- **If General Context (0)**: Uses a general-purpose LLM like LLaMA 2.

**Implementation**: This decision-making is crucial for accurate and context-aware response generation.

```python
if context_type == 1:
    # Process with LawGPT for legal context
    from law_gpt import LawGPT
    law_model = LawGPT()
    response = law_model.generate_response(keywords, sentiment)
else:
    # Process with General LLM for non-legal context
    from llama_model import LLaMA2
    general_model = LLaMA2()
    response = general_model.generate_response(keywords, sentiment)
```

## 8. Hosting on Azure
**Purpose**: Hosts the entire application on Azure for scalable, secure, and accessible deployment.

**Implementation**:
- **Azure Setup**: Configure an Azure VM or App Service with enough resources (CPU, GPU, RAM) to handle concurrent requests.
- **API Integration**: Use Azure API Management for secure and rate-limited API access.

```bash
# Azure CLI commands to set up the environment
az group create --name SecureAIResourceGroup --location eastus

az vm create --resource-group SecureAIResourceGroup --name SecureAIChatbotVM --image UbuntuLTS --admin-username azureuser --generate-ssh-keys

az vm open-port --resource-group SecureAIResourceGroup --name SecureAIChatbotVM --port 80 --priority 1001

# Deploy the application using Docker or direct code upload
az webapp up --name secure-ai-chatbot --resource-group SecureAIResourceGroup --plan AppServicePlan
```

## 9. Standard Operating Procedures (SOP)
- **Pre-Deployment Checklist**:
  - Ensure Azure VMs are configured and secure.
  - Validate all API keys and access controls are correctly set.
  - Test all LLM models locally with dummy data to verify responses.
- **Deployment Steps**:
  - Set up the Azure environment following the configuration steps outlined above.
  - Deploy the code using Docker, ensuring all dependencies are met (`requirements.txt`).
  - Monitor system performance and adjust VM resources as necessary for scaling.
- **Post-Deployment**:
  - Regularly update LLM models and NLP pipelines as needed.
  - Conduct security audits periodically to ensure compliance with data privacy laws.
  - Set up logging and monitoring using Azure Monitor for real-time insights and issue tracking.

## Screenshots and Diagrams
- **Flowchart 1**: Complete Project Flowchart - Shows how data moves through each layer from user input to final output.
- **Flowchart 2**: Updated Flowchart with Legal Context Focus - Highlights adjustments in the flow for better handling of legal contexts.
