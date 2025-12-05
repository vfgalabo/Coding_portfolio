# AI, Data Engineering, and Scientific Computing Portfolio

This repository showcases a range of projects across **Deep Learning (PyTorch)**, **Conversational AI**, and **Scalable Data Engineering (ETL)**. The projects demonstrate expertise in full-stack implementation, from raw data acquisition to final model validation.

---

## 🎯 Technical Skillset

| Category | Primary Technologies/Concepts | Projects Demonstrated |
| :--- | :--- | :--- |
| **Deep Learning (DL)** | **PyTorch**, CNNs, Transfer Learning, Validation Strategies, GPU Migration. | CIFAR-10 Classifier, Zoobot Finetuning for galaxy classification|
| **Conversational AI** | LLMs, RAG, Tool Use, **Secure Sandboxing**, Streamlit, Modular Architecture. | RAG Agent (PDF Summarizer), Coding Tool Agent |
| **Data Engineering (ETL)** | **Pandas**, **Selenium**, API Interception, Multi-Stage Pipelines, Data Consolidation. | Shanghai Ranking ETL Project |
| **Algorithms** | **Q-Learning**, Reinforcement Learning (RL), Custom Environment Design, Exploration/Exploitation. | Mars Rover RL Agent |
| **Scientific Computing** | **CPNest** Algorithm, MCMC Sampling, Parameter Estimation, Observational Data Analysis. | CPNest Algorithm, Obs. Cosmology |
---

## 📂 Featured Projects

### 1. Deep Learning: Image Classification (PyTorch CNN)
**Description:** A complete PyTorch pipeline for image classification built on the CIFAR-10 dataset. The project demonstrates core CNN architecture, rigorous **train/validation splitting**, and advanced metrics like per-class accuracy to analyze model performance.

### 2. Conversational AI: Secure Tool Agents
**Description:** A pair of Streamlit applications featuring Large Language Models (LLMs) used for: 1) Document summarization via Retrieval-Augmented Generation (RAG), and 2) **Securely executing code** to handle complex computational queries within a restricted sandbox environment.

### 3. Data Engineering: Hierarchical ETL Pipeline
**Description:** A high-complexity ETL project that scrapes dynamic university ranking data from the ShanghaiRanking website. The pipeline is architected for **scalability**, using a **two-stage Pandas consolidation process** to synthesize hundreds of files and inject hierarchical metadata.

### 4. THE Rankings Scraper (API Interception): 
**Description:** A highly efficient scraper that bypasses traditional, slow browser rendering by using API interception to directly extract pre-rendered JSON data. This showcases the ability to optimize acquisition pipelines for maximum speed and stability.

### 5. Specialized Algorithms: Mars Rover RL Agent
**Description:** An implementation of the **Q-Learning** algorithm to train an agent to navigate a custom 2D grid-world. The project focuses on defining the state/action space and managing the exploration-exploitation trade-off to find the optimal policy.

### 6. Scientific Computing & Parameter Estimation
**Description:** A project focused on advanced statistical inference using Type Ia Supernovae (SN Ia) data from the **Supernova Cosmology Project** (Perlmutter et al. 1999). The workflow involves detailed astronomical preprocessing—including **host galaxy light subtraction** and **K-correction** to fit the SN light curves—to yield the **peak apparent magnitude** and **stretch factor ($s$)**. The core statistical task involves applying the **CPNest nested sampling algorithm** for **high-dimensional parameter estimation** of key cosmological parameters ($\Omega_{\Lambda}, \Omega_{M}$) from the resulting Hubble diagram.

### 7. Deep Learning: Advanced Transfer Learning (Zoobot)
**Description:** A pipeline demonstrating the effective use of transfer learning by fine-tuning the Zoobot **ConvNeXt** model on the GalaxyMNIST dataset. The project validated the critical need for GPU acceleration and achieved $\mathbf{88.85\%}$ classification accuracy, with systematic error analysis revealing structural ambiguities between 'smooth_cigar' and 'edge_on_disk' galaxy classes.

## 🤝 Project Co-Development Acknowledgment

This portfolio was developed by [Vanya Fernandez Galabo] and utilized **Gemini 2.5 Flash** (a generative AI model by Google) as a dedicated **Co-Pilot and Technical Consultant** across multiple projects.

Gemini's assistance was instrumental in accelerating the most specialized and architecturally complex phases of development, including:

### 1. Advanced Agent Systems (RAG Agent (PDF Summarizer) & Coding Tool Agent)
* **Modular Architecture:** Establishing the clean, scalable file structure (`agent_core.py`, `core/tools.py`) for both Streamlit applications.
* **Security Hardening:** Implementing the restricted execution sandbox for the Python tool and advising on secure **Streamlit Secrets** management for API keys.
* **Error Management:** Designing robust logic to handle ambiguous user prompts and manage external API quota constraints (Error 429).

### 2. Deep Learning & Specialized Algorithms (Mars Rover RL & Pytorch CNN Architecture)
* **Algorithmic Scaffolding:** Provided the initial logical scaffolding for the Mars Rover Q-Learning Agent environment definition (state/action space, reward logic).
* **PyTorch CNN Architecture Review:** Guiding the development of the custom Convolutional Neural Network (CNN) for the CIFAR-10 classifier, reviewing the layer definitions and ensuring correct tensor flow.
* **Validation Strategy:** Advising on the implementation of a train/validation data splitting (torch.utils.data.random_split) and the associated validation loop to ensure accurate model performance tracking.
* **Analysis Plots Streamlining for Zoobot project:** Streamlined the conversion of raw prediction data into advanced, interpretable visualizations (e.g., Residual Distribution Plot Per Class and Per-Class Accuracy Chart) and advised on aesthetic choices for professional presentation of the visualizations.

### 3. Data Engineering & ETL Pipelines
* **Script Synthesis and Optimization:** Providing architectural guidance to synthesize multiple scraping scripts into a scalable, hierarchical two-step ETL process for the Shanghai scraping project.

### 3. Documentation & Review
* Ensuring project compliance with professional best practices (e.g., `.gitignore`, `requirements.txt`).


The repository owner maintained full control over **final code implementation, hyperparameter tuning, validation, and architectural decisions** across all projects.