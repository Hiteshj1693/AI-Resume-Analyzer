print("Start")

# import PyPDF2

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         num_pages = len(reader.pages)
#         for page_num in range(num_pages):
#             page = reader.pages[page_num]
#             text += page.extract_text()
#     return text

# pdf_file_path = "/Users/nitinjethava/Downloads/Study/AI/AI-Resume-Analyzer/HiteshResume.pdf"
# resume_text = extract_text_from_pdf(pdf_file_path)
# print(resume_text)


from pyresparser import ResumeParser

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        parser = ResumeParser(file)
        parsed_data = parser.get_extracted_data()
        text = parsed_data["text"]
    return text

pdf_file_path = "/Users/nitinjethava/Downloads/Study/AI/AI-Resume-Analyzer/HiteshResume.pdf"
resume_text = extract_text_from_pdf(pdf_file_path)
print(resume_text)
