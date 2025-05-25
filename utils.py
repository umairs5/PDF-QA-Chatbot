# utils.py
import os

import cassio
import re
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores.cassandra import Cassandra
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Your secrets (use dotenv or config file for production)
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set up Groq LLM
def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=GROQ_API_KEY
    )

# Initialize or reset the vector store
def setup_astra_vectorstore(reset=False):
    cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Cassandra(
        embedding=embedding,
        table_name="qa_pdf",
        session=None,
        keyspace=None
    )

    if reset:
        print("Resetting DB table...")
        vectorstore.delete_collection()

    return vectorstore

# Process and split the uploaded PDF
def process_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    raw_text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content

    cleaned_text = re.sub(r'\t', ' ', raw_text)
    cleaned_text = re.sub(r'\n+', '\n', cleaned_text)
    cleaned_text = re.sub(r' +', ' ', cleaned_text).strip()

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(cleaned_text)
    return chunks
