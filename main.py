from pdf2image import convert_from_path
import os

pdf_path = r"PPT.pdf"
popple_path = r"C:\Users\Harshal\Desktop\Py_Project\Demo.py\poppler-24.02.0\Library\bin"

if not os.path.isfile(pdf_path):
    raise FileNotFoundError(f"PDF file not found: {pdf_path}")

try:
    old_pdf = convert_from_path(pdf_path, poppler_path=popple_path)
except Exception as e:
    print(f"An error occurred: {e}")
    raise

for i in range(len(old_pdf)):
    old_pdf[i].save(f"new{i}.jpg", "JPEG")
