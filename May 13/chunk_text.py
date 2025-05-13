import fitz  # PyMuPDF

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Extract text from each page
    extracted_text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Get the page
        extracted_text += page.get_text()  # Extract text from the page

    return extracted_text

# Main function
if __name__ == "__main__":
    
    pdf_file = "C:/Users/nehav/Desktop/WEEK 2/May 13/sample.pdf"

    
    try:
        # Extract text from the specified PDF
        extracted_text = extract_text_from_pdf(pdf_file)
        
        # Print the extracted text (you can also save it to a file)
        print(extracted_text)
    except Exception as e:
        print(f"An error occurred: {e}")
