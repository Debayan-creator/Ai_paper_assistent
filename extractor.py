import fitz  # PyMuPDF
import pdfplumber

def extract_text(file):
    """Try PyMuPDF first (fast), then PDFPlumber. Works with Streamlit file object."""
    # --- Attempt 1: PyMuPDF from in-memory stream ---
    try:
        file.seek(0)
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
        if text.strip():
            return text
    except Exception:
        pass

    # --- Attempt 2: PDFPlumber fallback (needs a seekable file-like) ---
    try:
        file.seek(0)
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
                text += "\n"
        return text
    except Exception as e:
        return f"Failed to extract text: {str(e)}"
