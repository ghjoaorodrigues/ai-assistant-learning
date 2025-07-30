# main.py

from app.parser import extract_text_from_pdf, chunk_text

if __name__ == '__main__':
    pdf_path = "data/en.subject.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(f"Total characters extracted: {len(text)}")
    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")
    print(f"\nFirst chunk: {chunks[0]}\n")

