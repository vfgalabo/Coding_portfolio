## 🤝 Project Co-Development Acknowledgment

This portfolio utilized **Gemini 2.5 Flash** (a generative AI model by Google) as a dedicated **Co-Pilot and Technical Consultant** across multiple projects.

Gemini's assistance was instrumental in accelerating the most specialized and architecturally complex phases of development, including:

### 1. Advanced Agent Systems (RAG Agent (PDF Summarizer) & Coding Tool Agent)
* **Modular Architecture:** Establishing the clean, scalable file structure (`agent_core.py`, `core/tools.py`) for both Streamlit applications.
* **Security Hardening:** Implementing the **restricted execution sandbox** for the Python tool and advising on secure **Streamlit Secrets** management for API keys.
* **Error Management:** Designing robust logic to handle ambiguous user prompts and gracefully manage external API quota constraints (Error 429).

### 2. Deep Learning & Specialized Algorithms (Mars Rover RL & Pytorch CNN Architecture)
* **Algorithmic Scaffolding:** Structuring the core logic for the **Mars Rover Q-Learning Agent** and defining the custom environment (GridWorld, boundary logic).
* **PyTorch CNN Architecture Review:** Guiding the development of the custom Convolutional Neural Network (CNN) for the CIFAR-10 classifier, reviewing the layer definitions and ensuring correct tensor flow.
* **Validation Strategy:** Advising on the implementation of a train/validation data splitting (torch.utils.data.random_split) and the associated validation loop to ensure accurate model performance tracking.

### 3. Data Engineering & ETL Pipelines
* **Script Synthesis and Optimization:** Providing architectural guidance to synthesize multiple scraping scripts into a scalable, hierarchical two-step ETL process for the Shanghai scraping project.

### 3. Documentation & Review
* Ensuring project compliance with professional best practices (e.g., `.gitignore`, `requirements.txt`).


The repository owner maintained full control over **final code implementation, hyperparameter tuning, validation, and architectural decisions** across all projects.