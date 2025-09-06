def clean_text(text):
    """Basic cleanup: collapse whitespace/newlines."""
    return " ".join(text.split())
