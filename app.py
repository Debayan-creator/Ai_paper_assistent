import streamlit as st
from PyPDF2 import PdfReader
import fitz  # PyMuPDF

# Constraints
Max_file_size = 20  # MB
Max_pages = 100

# Validation function
def validate_pdf(file):
    if file is None:
        return False, "No file uploaded."

    if not hasattr(file, "getbuffer"):  # ensures it's a Streamlit UploadedFile
        return False, "Invalid file type. Please upload a PDF."

    # Check size
    size = len(file.getbuffer()) / (1024 * 1024)  # MB
    if size > Max_file_size:
        return False, f"File size exceeds {Max_file_size} MB limit."

    # Check PDF pages
    try:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        if num_pages > Max_pages:
            return False, f"File has {num_pages} pages, exceeds {Max_pages} pages limit."
    except Exception as e:
        return False, f"Error reading PDF file: {e}"

    return True, "PDF is valid."


# Streamlit UI
st.title("Upload Your Research Paper")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Open directly from bytes
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    
    st.text_area("Extracted Text", text[:2000])
