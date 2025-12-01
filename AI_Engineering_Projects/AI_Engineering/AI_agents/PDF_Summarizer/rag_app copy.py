import getpass
import os
import streamlit as st
import tempfile  
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_core.messages import HumanMessage, ToolMessage
from langchain.chat_models import init_chat_model
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import nest_asyncio
# Apply nest_asyncio to allow nested event loops in Streamlit
nest_asyncio.apply() 

# --- App Layout and User Input ---
# Set the page configuration and title
st.set_page_config(page_title="PDF Summarizer and Q&A", layout="wide")
st.title("📚 PDF Summarizer and Reader")
st.write("Upload a PDF file and ask questions about its content.")

# Add a file uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Add a text input for the user's question
user_query = st.text_input("Enter your question about the PDF:", disabled=not uploaded_file)

# --- Main Logic ---
# The rest of the code will now be inside this block
if uploaded_file and user_query:
    # API Key for Google Gemini 
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

    # --- Initialize the model ---
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    # Create a secure temporary file to store the uploaded PDF
    # This ensures that the file is stored securely and can be deleted after processing
    # Using NamedTemporaryFile to ensure the file is deleted after use
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    try:
        # Now use the secure, temporary path to load the document
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        # Split the pdf into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)

        # Create a vector store:
        # Use Google Generative AI embeddings to create a vector store from the document chunks
        # This allows the model to retrieve relevant information from the document
        # when answering questions
        embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_documents(chunks, embeddings_model)   
        retriever = vector_store.as_retriever()
    
        # Create the chain that combines the retriever with the language model
        # This chain will use the model to answer questions based on the retrieved information
        # The "refine" chain type allows the model to iteratively improve its answer
        qa_chain = RetrievalQA.from_chain_type(
            llm=model,
            chain_type="refine",    # Use "refine" to improve the answer iteratively
            retriever=retriever
        )


        # Invoke the chain with the user's question and display the response
        with st.spinner("Thinking..."):
            response = qa_chain.invoke({"query": user_query})
            st.subheader("Answer:")
            st.write(response["result"])
    finally:
        # This block ensures the temporary file is deleted even if an error occurs
        os.remove(temp_file_path)
