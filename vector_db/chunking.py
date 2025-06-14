import os
from PyPDF2 import PdfReader
from typing import List, Dict
import tiktoken

# Optional: Change chunking strategy if needed
CHUNK_SIZE = 400  # number of tokens or characters
CHUNK_OVERLAP = 50

def load_pdf_text(pdf_path: str) -> List[str]:
    """Extract text from each page of a PDF."""
    print("""Extract text from each page of a PDF.""")
    reader = PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        pages.append(text.strip())
    return pages

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    """Chunk the text using character-based splitting with overlap."""
    print("""Chunk the text using character-based splitting with overlap.""")
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def get_all_pdf_chunks() -> List[Dict]:
    """Process all PDFs and return a list of chunks with metadata."""
    print("""Process all PDFs and return a list of chunks with metadata.""")
    chunks_with_metadata = []
    print(os.listdir("."))
    for filename in os.listdir("."):
        if filename.endswith(".pdf"):
            pages = load_pdf_text(filename)
            for i, page_text in enumerate(pages):
                chunks = chunk_text(page_text, CHUNK_SIZE, CHUNK_OVERLAP)
                for j, chunk in enumerate(chunks):
                    chunks_with_metadata.append({
                        "content": chunk,
                        "source_file": filename,
                        "page": i + 1
                    })
    return chunks_with_metadata

if __name__ == "__main__":
    all_chunks = get_all_pdf_chunks()
    print(f"✅ Loaded {len(all_chunks)} chunks from PDFs.")
    print(all_chunks[0]) 
