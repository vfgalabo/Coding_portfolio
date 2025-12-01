import streamlit as st
import time

# Import the function that runs the agent
from agent_core import get_agent_response

# --- Streamlit App Interface ---
st.set_page_config(page_title="Agentic AI Demo", layout="wide")
st.title("Agentic AI Demo with Python REPL and Tavily Search")
st.write("Ask the agent anything, and it will give you a response.")

# --- User Input Section ---
# Use a form to wrap the text input and button for better key management and execution control
with st.form("agent_query_form"):
    user_query = st.text_input("Enter your query here:")
    submit_button = st.form_submit_button("Ask Agent")

# This logic checks if the user has entered a query and clicked the button
if submit_button and user_query: 
    # Use st.spinner to give the user visual feedback that the agent is thinking
    with st.spinner("Agent is working..."):
        # Call the core logic function
        get_agent_response(user_query)

# --- Acknowledgement Block ---
st.markdown("---")
st.markdown(
    """
    ### 🤝 Development and Acceleration Acknowledgment
    
    This Agentic AI application was developed with technical assistance from **Gemini 2.5 Flash** (a generative AI model by Google). 
    
    The model was utilized as a **specialized co-pilot** to accelerate key project phases, including:
    
    * **Architecture & Modularity:** Providing recommendations for a robust, modular file structure (`app.py`, `agent_core.py`, `core/tools.py`).
    * **Security hardening:** Advising on and implementing the **restricted execution environment** for the `python_repl` tool, addressing potential **Remote Code Execution (RCE)** risks.
    * **Logic Synthesis:** Expediting the setup of the **LangChain agent orchestration** and secure Streamlit integration.
    
    The agent's logic was **curated, integrated, and deployed by the repository owner**, following a standard co-development workflow.
    """
)
# -----------------------------