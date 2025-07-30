# app/parser.py

import fitz # PyMuPDF

def extract_text_from_pdf(file_path):
    """Extract text from all pages of the PDF"""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    """Split the text in chunks with overlap"""
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks