import fitz
import os
from app.config import PDF_FOLDER

def load_pdf(file):
    filepath = os.path.join(PDF_FOLDER, file.filename)
    with open(filepath, "wb") as f:
        f.write(file.file.read())

    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()

    return text