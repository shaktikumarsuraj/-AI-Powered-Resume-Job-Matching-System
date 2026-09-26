from pypdf import PdfReader
file_path= r"C:\Users\shakt\Downloads\Window-c\langchain\Resume_shakti.pdf"

def extract_text_from_pdf(file_path):
    reader=PdfReader(file_path)
    text=""
    for pages in reader.pages:
        text+=pages.extract_text() or ""

    return text 
# resume_text= extract_text_from_pdf(file_path)
# print(resume_text)