# Agentic AI Demo with Python REPL and Web Search

This project is a Streamlit application that showcases an AI agent capable of executing Python code and performing web searches. It demonstrates the use of LangChain's tool-calling capabilities to allow a large language model to interact with external systems to answer queries.

## 🚀 Features

* **Python REPL Tool**: The agent can interpret and execute Python code snippets to perform calculations, solve programming tasks, and answer complex mathematical queries.
* **Web Search Tool**: Integrated with the **Tavily Search API**, the agent can search the web for real-time information to answer questions about current events or topics outside of its training data.
* **Intelligent Tool Selection**: The agent automatically decides which tool (Python REPL or Web Search) is needed to fulfill a user's request.
* **Streamlit UI**: A user-friendly web interface built with Streamlit for easy interaction.

## 🛠️ How to Run

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/vfgalabo/Coding_portfolio.git](https://github.com/vfgalabo/Coding_portfolio.git)
    cd AI_Engineering_Projects/AI_agents/Coding_agent
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up API Keys**:
    You will need a Google Gemini API key and a Tavily Search API key. It's recommended to store these in your environment variables.
    * Create a `.env` file or use your system's environment variables.
    * Alternatively, you can manually enter the keys when prompted by the application.

4.  **Run the Application**:
    ```bash
    streamlit run agent_app.py
    ```

## 🖼️ Screenshots

### The Application in Action

This screenshot shows the agent answering a question about the current population of Tokyo. The agent intelligently recognized that it needed to use its **Tavily Search tool** to get up-to-date information from the web.


![An image of the Agentic AI app in action.](https://raw.githubusercontent.com/vfgalabo/Coding_portfolio/master/AI_Engineering_Projects/AI_Engineering/AI_agents/Coding_agent/assets/agent_1.png)

### The Agent's Response

This screenshot shows the agent solving a mathematical query by generating and executing Python code. The agent used its **Python REPL tool** to perform the vector dot product calculation.

![A close-up image of the agent's structured response.](https://raw.githubusercontent.com/vfgalabo/Coding_portfolio/master/AI_Engineering_Projects/AI_Engineering/AI_agents/Coding_agent/assets/agent_2.png)

## 📦 Dependencies

* `streamlit`
* `langchain`
* `langchain_google_genai`
* `langchain_tavily`
* `pydantic`

## Author

[Vanya Fernandez Galabo]