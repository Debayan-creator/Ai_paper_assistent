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

# After showing preview
st.markdown("### Ask a Question or Request a Summary")

# Text input for the prompt
user_prompt = st.text_area("Enter your question or prompt:")

if st.button("Generate Answer"):
    if user_prompt.strip():
        st.info("Processing your request...")
        from summarizer import summarize_text  # Ensure your API key is set there
        
        # Combine user prompt with extracted text
        combined_prompt = f"User question: {user_prompt}\n\nDocument content:\n{text}"
        response = summarize_text(combined_prompt)
        
        st.subheader("AI Response")
        st.write(response)
    else:
        st.warning("Please enter a question or prompt.")
