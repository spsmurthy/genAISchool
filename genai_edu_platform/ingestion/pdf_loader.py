import fitz  # PyMuPDF

def load_and_chunk_pdf(file_path, chunk_size=500):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks