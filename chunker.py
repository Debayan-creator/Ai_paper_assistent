def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks for embeddings."""
    chunks = []
    start = 0
    step = max(1, chunk_size - overlap)
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += step
    return chunks
