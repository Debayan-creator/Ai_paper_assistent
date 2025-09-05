import streamlit as st
from upload_handler import handle_upload
from extractor import extract_text

st.title("AI Research Paper Assistant")

uploaded_files = st.file_uploader(
    "Upload research papers", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        if handle_upload(file):
            # Reset pointer after validation (PyPDF2 may advance the stream)
            file.seek(0)
            text = extract_text(file)
            st.success(f"Extracted {len(text)} characters from {file.name}")
            st.text_area("Preview", text[:2000])
        else:
            st.error(f"File '{file.name}' is invalid or too large.")
