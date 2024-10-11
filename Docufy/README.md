# Docufy: An Intelligent Document Querying System

**Credits** Harsh Chinchakar - harshchinchakar33@gmail.com
**Docufy** is a powerful AI-based document querying tool, similar to Google's **NotebookLM**, designed for interacting with and retrieving information from documents. But Docufy goes a step further by providing responses to queries that may not have direct answers within the document, explicitly stating when information is not available in the provided content. This makes Docufy not only a document-centric AI assistant but also a versatile conversational agent capable of addressing broader queries.

## Table of Contents
- [Key Features](#key-features)
- [How Does Docufy Differ from NotebookLM?](#how-does-docufy-differ-from-notebooklm)
- [Architecture Overview](#architecture-overview)
- [Setup and Installation](#setup-and-installation)
- [Usage Guide](#usage-guide)
  - [Uploading Documents](#uploading-documents)
  - [Querying the Document](#querying-the-document)
  - [Using the Chat History Feature](#using-the-chat-history-feature)
  - [Handling Queries Outside Document Context](#handling-queries-outside-document-context)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Key Features
- **Document-Centric and General Querying**: Docufy is designed to answer queries directly based on the content of uploaded PDFs, as well as provide intelligent responses when the information is outside the document's scope.
- **Explicit Non-Availability Response**: When a question is asked that cannot be answered using the document content, Docufy explicitly states that the information is not available in the provided document.
- **Query History Management**: Docufy maintains a history of user interactions, allowing users to reference previous queries and responses seamlessly.
- **Customizable NLP Pipeline**: Uses a combination of semantic search and keyword-based techniques to find the most relevant sections in a document, ensuring high accuracy in retrieval.
- **Secure AI Capabilities**: Integrates a security layer for adversarial input detection, ensuring that user data is processed safely.

## How Does Docufy Differ from NotebookLM?
- **Out-of-Document Query Responses**: While both NotebookLM and Docufy can interpret and analyze document content, Docufy uniquely handles out-of-document queries by stating when the requested information is not found within the document.
- **Focus on Security**: With additional layers like adversarial attack detection, encryption, and content filtering, Docufy is designed with security in mind, making it suitable for sensitive data handling.
- **History Tracking**: Docufy’s chat history feature allows users to track previous conversations, which can be crucial when working on long-term research or projects.
- **Versatile Integration**: The system is designed to be easily integrated into various environments, such as cloud platforms like Google Colab or standalone server setups.

## Architecture Overview
The architecture of Docufy includes the following layers and components:
1. **File Upload and Processing**: Users can upload PDF documents through an intuitive interface.
2. **Document Chunking**: Breaks down large documents into manageable chunks using context-aware chunking techniques.
3. **Semantic and Keyword-Based Search**: Employs hybrid search techniques using embeddings for semantic understanding and keyword-based retrieval to identify relevant sections.
4. **Context-Aware Response Generation**: Utilizes large language models (LLMs) to generate responses based on retrieved chunks and provides answers outside of document content when necessary.
5. **Chat History Management**: Stores conversation history, enabling users to refer back to previous queries and responses for context.

## Setup and Installation
To set up Docufy, follow the steps below:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/docufy.git
    cd docufy
    ```

2. **Install the Required Packages**:
    Ensure you have Python 3.8+ installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup API Keys** (if required):
    For models like LLaMA or other LLM services, place your API keys in a `.env` file:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application**:
    Start the application using:
    ```bash
    python app.py
    ```

## Usage Guide
### Uploading Documents
1. **Upload a PDF**: Users can drag and drop a PDF file into the interface.
2. **Document Processing**: Docufy processes the document by extracting text and generating context-aware embeddings for each chunk of content.

### Querying the Document
- **Ask Questions Based on Document Content**: Users can ask questions directly related to the document's content. Docufy will extract relevant chunks and generate precise answers.
- **Follow-Up Questions**: Users can ask follow-up questions to dive deeper into the context of previous queries, utilizing the chat history for reference.

### Using the Chat History Feature
- **Persistent Context**: Docufy maintains context across multiple queries by storing chat history. This enables users to build on previous conversations without needing to re-upload documents or restate context.
- **History File Storage**: Each conversation session is saved in a history file, which can be accessed or deleted as needed for privacy.

### Handling Queries Outside Document Context
- **Explicitly Stating Non-Availability**: If a user’s question pertains to information not present in the document, Docufy will respond with: 
    ```
    "The requested information is not found in the uploaded document. Here is what I can infer outside the document context..."
    ```
- **General Knowledge Integration**: When a query is outside the document's scope, Docufy can tap into general knowledge using a pre-configured LLM, making it suitable for broader research applications.

## Future Enhancements
- **Real-Time PDF Annotation**: Add features to annotate PDFs directly based on user queries.
- **Advanced Model Integration**: Explore integration with newer models and provide an option for users to select from a list of LLMs.
- **User Authentication**: Implement user authentication for personalized settings and secure access.

## Contributing
We welcome contributions to improve Docufy. If you’d like to contribute, please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push the changes:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## License
Docufy is licensed under the MIT License. See `LICENSE` for more information.
