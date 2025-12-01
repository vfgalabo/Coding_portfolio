import os
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.chains import RetrievalQA
from core.tools import get_vector_store_retriever # Import our tool!

# --- Model and API Key Initialization ---

# Use st.secrets to securely retrieve the key
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("⚠️ Gemini API Key is missing. Please ensure it is set in .streamlit/secrets.toml.")
    st.stop()
else:
    # Set the key in os.environ for LangChain components that require it
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    
    # Initialize the model (only runs if the key is present)
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# --- Agent Execution Function ---

def run_rag_query(uploaded_file, user_query):
    """
    Creates the RAG chain from the uploaded file and invokes it with the user query.
    """
    
    # 1. Get the retriever from the uploaded file
    retriever = get_vector_store_retriever(uploaded_file)
    
    # 2. Create the RAG chain (RetrievalQA)
    qa_chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="refine",
        retriever=retriever
    )

    # 3. Invoke the chain and get the response
    with st.spinner("Thinking..."):
        response = qa_chain.invoke({"query": user_query})
        
    return response["result"]