
# RAG-LLM-Architecture-Assistant

A **Retrieval-Augmented Generation (RAG)** pipeline that uses PDF as a knowledge base to answer questions about **Large Language Model architectures**.

It leverages:

- [**Ollama**](https://ollama.com/) for local LLM inference
- [**ChromaDB**](https://www.trychroma.com/) for vector storage

This enables **offline**, **private** and **efficient** AI-powered Q&A.

---

## 🚀 Features

-  Answers architecture-related queries using LLMs
-  Fully local: no data leaves your machine
-  Fast retrieval with vector search via ChromaDB

---

## 📦 Tech Stack

- **LLM Inference**: Ollama
- **Vector Store**: ChromaDB
- **Language**: Python

---
Follow these steps to set up the project on your local machine:
- pip install -r requirements.txt
- Place your documents inside the pdfs/ folder
- run main.py 


## 🙏 Acknowledgements

This project is based on the original work from (https://github.com/techwithtim/LocalAIAgentWithRAG)

I have modified and extended the code to build a customized version focused on offline PDF-based RAG for LLM architectures



