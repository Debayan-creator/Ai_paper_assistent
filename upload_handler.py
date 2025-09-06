from PyPDF2 import PdfReader

MAX_FILE_SIZE_MB = 20
MAX_PAGES = 100

def handle_upload(file):
    """Validate PDF upload for size and page count."""
    size_mb = len(file.getbuffer()) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        return False

    try:
        # PdfReader may advance the stream; caller should seek(0) after this
        reader = PdfReader(file)
        if len(reader.pages) > MAX_PAGES:
            return False
    except Exception:
        return False
    return True
