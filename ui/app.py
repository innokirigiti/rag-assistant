import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")
if not API_BASE_URL:
    raise ValueError("API_BASE_URL not found in .env")

st.write("""
# Welcome to DocAI - A RAG AI agent
""")
    
    

st.title("Upload a PDF")

uploaded_file = st.file_uploader(
    label="Choose a PDF file",
    type=["pdf"]
)

def upload_file(file):

    
    UPLOAD_URL = f"{API_BASE_URL}/uploadpdf"

    with st.spinner("Uploading file..."):

        files = {
            "file": (file.name, file.getvalue(), "application/pdf")
        }

        response = requests.post(UPLOAD_URL, files=files)

        if response.status_code == 200:
            st.success("File uploaded successfully!")
            st.json(response.json())
        else:
            st.error("Upload failed")


if uploaded_file is not None:

    st.write(f"Selected file: **{uploaded_file.name}**")

    st.button(
        "Upload",
        on_click=upload_file,
        args=(uploaded_file,)
    )