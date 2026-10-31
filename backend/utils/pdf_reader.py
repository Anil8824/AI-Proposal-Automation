import fitz  # PyMuPDF


# --------------------------------------------------
# Extract Text from PDF
# --------------------------------------------------

def extract_text_from_pdf(file_path):
    """
    Extracts readable text from a PDF file.
    Returns an empty string if extraction fails.
    """

    try:
        text = ""

        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text()

        return text.strip()

    except Exception as e:
        print(f"PDF Extraction Error: {e}")
        return ""