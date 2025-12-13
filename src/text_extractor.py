import fitz


# Extract text from PDF using PyMuPDF (fitz)
def extract_text_from_pdf(pdf_path):
    # Open the PDF document
    with fitz.open(pdf_path) as doc:
        # Extract text from each page
        pages = [page.get_text() for page in doc]
    return pages