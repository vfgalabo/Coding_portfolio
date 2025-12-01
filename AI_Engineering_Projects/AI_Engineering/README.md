# 🤖 AI Agents with Web Search, Python Tool and PDF Summarization

This repository showcases two distinct AI agent projects, both built with Streamlit and LangChain, demonstrating the power of Large Language Models (LLMs) to interact with external data sources. The projects are designed to be user-friendly, providing a seamless experience for anyone interested in exploring the capabilities of modern AI.

***

### 💻 Project 1: Agentic AI Demo with Python REPL and Web Search

This project features an AI agent that can intelligently choose between two tools to answer user queries: a **Python REPL Tool** and a **Web Search Tool**.

#### ✅ Core Functionality

* **Python REPL:** The agent uses this tool to perform complex calculations and execute code. For example, it can handle mathematical queries like vector dot products by generating and running Python code.
* **Web Search:** Integrated with the **Tavily Search API**, this tool allows the agent to find real-time, up-to-date information on the internet. This is particularly useful for questions about current events or topics not included in the model's training data.
* **Intelligent Tool Selection:** The agent analyses each query to determine the most appropriate tool to use, providing a dynamic and context-aware response.

***

### 📄 Project 2: PDF Summarizer and Reader

This project provides a powerful way to interact with PDF documents. It uses a **Retrieval-Augmented Generation (RAG)** system to allow users to ask questions about the content of any uploaded PDF.

#### ✅ Core Functionality

* **Document Q&A:** The application processes a user-uploaded PDF by splitting it into manageable chunks. It then uses **Google Gemini embeddings** to perform a **semantic search** and retrieve the most relevant sections of the document to answer a query.
* **Advanced Refine Chain:** To ensure coherent and comprehensive answers, the application employs a "refine" chain. This process allows the LLM to synthesize information from multiple document fragments, providing a response that considers the document's context as a whole.
* **FAISS Vector Store:** The retrieved document chunks are stored in a **FAISS vector store**, which is optimized for efficient similarity search, making the Q&A process fast and effective.

***
