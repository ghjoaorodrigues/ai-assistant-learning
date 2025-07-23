# Project 1: Building a Context-Aware PDF Chatbot with RAG and Vector Search

## Project Objective

Design and implement a lightweight chatbot that can intelligently answer questions based on the content of one or more PDF documents. It should use a Retrieval-Augmented Generation (RAG) architecture that retrieves relevant document chunks using embeddings and passes them as context to a Large Language Model (LLM).

## Key Concepts Covered

- LLMs (via OpenAI, Mistral, Claude, or local models)
- Embeddings (text turned into vectors for search)
- Vector databases (FAISS, Pinecone, Chroma)
- PDF parsing
- Chunking & token limits
- Prompt construction with context injection
- Basic web UI or CLI chatbot

## Tools & Stack

| Layer               | Tool Suggestions                         |
|---------------------|-------------------------------------------|
| LLM                 | OpenAI (e.g., `gpt-3.5-turbo`) or local (e.g., Ollama + Mistral) |
| Embeddings          | OpenAI, HuggingFace, or `sentence-transformers` |
| Vector DB           | FAISS (simple), Chroma (easy), or Pinecone (hosted) |
| PDF Processing      | `PyMuPDF` (`fitz`) or `pdfplumber`        |
| Framework           | Python (FastAPI for later extension)      |
| Interface           | CLI / Streamlit (optional, for interactivity) |

## Suggested Folder Structure

pdf-chatbot/
│
├── data/                  # PDF files
├── embeddings/            # Saved vector DBs
├── prompts/               # Prompt templates
├── app/                   # Core logic
│   ├── parser.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── chatbot.py
│   └── config.py
├── main.py                # Entry script
├── requirements.txt
└── README.md

## Milestones

1. Parse PDFs and chunk the text intelligently
2. Generate and store embeddings using a model like `text-embedding-ada-002` or `all-MiniLM`
3. Query chunks using semantic similarity (via FAISS)
4. Build a function to construct prompts with relevant context
5. Use an LLM to generate a response based on prompt
6. (Optional) Add a CLI or basic web UI (e.g., Streamlit or Flask)

## Bonus Challenges

- Summarization of long PDFs
- Support multiple PDFs (multi-doc retrieval)
- Add memory across conversations
- Limit token usage dynamically

