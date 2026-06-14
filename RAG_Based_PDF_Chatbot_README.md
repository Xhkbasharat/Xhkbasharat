# RAG-Based PDF Chatbot (Chat with Documents)

A Retrieval-Augmented Generation (RAG) application that enables users to
upload PDF documents and ask natural language questions about their
contents. The system retrieves the most relevant document passages using
vector search and generates context-aware answers with a Large Language
Model (LLM).

## Features

-   Upload one or more PDF documents
-   Automatic text extraction and chunking
-   Embedding generation and vector indexing
-   Semantic search with FAISS
-   Context-aware question answering
-   Conversation history support
-   Clean web interface for interactive document chat

## Tech Stack

-   Python
-   LangChain
-   FAISS
-   Large Language Models (LLMs)
-   Hugging Face Embeddings or OpenAI Embeddings
-   Flask or Streamlit
-   PyPDF
-   HTML, CSS, JavaScript

## Project Workflow

1.  Upload PDF documents.
2.  Extract and split text into chunks.
3.  Create embeddings for each chunk.
4.  Store embeddings in a FAISS vector database.
5.  Retrieve the most relevant chunks for a user query.
6.  Send the retrieved context to the LLM.
7.  Return an accurate, context-aware response.

## Future Enhancements

-   Support for DOCX, TXT, and PowerPoint files
-   Multi-document knowledge base
-   Source citation highlighting
-   User authentication and document management
-   Cloud deployment with scalable vector databases

## License

This project is intended for educational and research purposes.
