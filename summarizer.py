from transformers import pipeline
from sentence_transformers import SentenceTransformer

# Much smaller model (better for local use)
summarizer = pipeline(
    "text-generation",
    model="facebook/opt-1.3b"  # Only ~2GB
)

def summarize_text(text):
    prompt = f"Summarize this research paper:\n\n{text}\n\nSummary:"
    result = summarizer(prompt, max_new_tokens=250, do_sample=True, temperature=0.3)
    return result[0]['generated_text']