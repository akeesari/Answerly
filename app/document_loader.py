import os
from typing import List
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(filepath: str) -> str:
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(filepath: str) -> str:
    doc = docx.Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents(folder_path: str) -> List[str]:
    chunks = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(full_path)
        elif filename.lower().endswith(".docx"):
            text = extract_text_from_docx(full_path)
        else:
            continue

        # Optional: Split into chunks if text is long
        for chunk in split_text(text, max_length=500):
            chunks.append(chunk.strip())

    return chunks

def split_text(text: str, max_length: int) -> List[str]:
    sentences = text.split(". ")
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) < max_length:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "

    if current:
        chunks.append(current.strip())

    return chunks
