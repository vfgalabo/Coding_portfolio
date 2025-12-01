import os
import tempfile
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- Define the Vectorization Process ---

def get_vector_store_retriever(uploaded_file):
    """
    Loads an uploaded PDF, splits it into chunks, creates a FAISS vector store,
    and returns a retriever object.
    """
    temp_file_path = None
    
    # Create a secure temporary file to store the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    try:
        # Load the document from the temporary path
        pdf_reader = PdfReader(temp_file_path)
        raw_text = ""
        # Look through each page in the PDF and extract the text
        for page in pdf_reader.pages:
            raw_text += page.extract_text() or "" 
        documents = [Document (page_content=raw_text, metadata={"source": uploaded_file.name} )]
        
        # Check if documents were loaded successfully 
        if len(raw_text.strip()) < 100:
            raise ValueError("The PDF file contains too little text to process effectively or is unreadable")
        
        # Split the pdf into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300, # Reduced chunk size for better context handling (for short documents)
            chunk_overlap=50
        )
        chunks = text_splitter.split_documents(documents)

        # Check if chunks were created successfully
        if not chunks:
            raise ValueError("Could not create text chunks from the document. The text may be too short or unreadable.")
        
        # Create the embeddings model and vector store
        embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_documents(chunks, embeddings_model) 
        
        # Return the retriever
        return vector_store.as_retriever()
        
    finally:
        # Important step: ensure the temporary file is deleted
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
