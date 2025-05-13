import fitz  # PyMuPDF
import os

def extract_pdf_text(filepath):
    """
    Extracts and returns all text from a PDF file.

    Parameters:
    - filepath (str): The path to the PDF file.

    Returns:
    - str: All text extracted from the PDF.
    """
    text = ""
    try:
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

if __name__ == "__main__":
    # Replace this with your actual PDF file name
    path_to_pdf = "sample.pdf"

    # Check if the file exists
    if not os.path.exists(path_to_pdf):
        print(f" File not found: {path_to_pdf}")
    else:
        extracted_text = extract_pdf_text(path_to_pdf)
        print(" Extracted Text:\n")
        print(extracted_text if extracted_text.strip() else "[No text found in PDF]")

