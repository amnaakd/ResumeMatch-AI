import fitz  # PyMuPDF
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file.
    """

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()