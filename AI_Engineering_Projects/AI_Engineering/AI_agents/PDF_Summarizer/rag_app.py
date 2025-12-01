import streamlit as st
import nest_asyncio
from agent_core import run_rag_query # Import our main execution function

# Apply nest_asyncio to allow nested event loops in Streamlit
nest_asyncio.apply() 

# --- App Layout and User Input ---
st.set_page_config(page_title="PDF Summarizer and Q&A", layout="wide")
st.title("📚 PDF Summarizer and Reader")
st.markdown("Upload a PDF file and ask questions about its content.")

# Add a file uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Add a text input for the user's question
# The input is disabled until a file is uploaded
user_query = st.text_input("Enter your question about the PDF:", disabled=not uploaded_file)

# --- Main Interaction Logic ---
if uploaded_file and user_query:
    # Check if the user has actually typed something meaningful
    if user_query.strip():
        # Call the orchestrator function
        try:
            st.subheader("Answer:")
            response_text = run_rag_query(uploaded_file, user_query)
            st.write(response_text)
            
        except Exception as e:
            st.error(f"An error occurred during processing: {e}")
            st.info("Please ensure your Gemini API Key is correct in `.streamlit/secrets.toml`.")


st.markdown("---")
st.markdown("""

### 🤝 Development Acknowledgment

This RAG application was built using a **co-development workflow** with technical assistance from **Gemini 2.5 Flash** (a generative AI model by Google). The development process involved distinct roles for the repository owner and Gemini, focusing on architecture, implementation, optimization, and refinement.

---

### ⚠️ Note on Embedding Quotas

Due to the constraints of the Google **Embedding API's free-tier quota**, the application may intermittently return a `429 Quota Exceeded` error when attempting to process new PDF documents. 
This is a common **rate-limiting constraint** applied by API providers to resource-intensive services. The application's design successfully handles this error, protecting the system from crashes, 
and will resume full functionality after the daily quota resets.
""")