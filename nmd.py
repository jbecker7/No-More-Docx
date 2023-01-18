import os
from docx2pdf import convert
from pathlib import Path

def convert_to_pdf(word_file_path):
    pdf_file_path = os.path.splitext(word_file_path)[0] + ".pdf"
    convert(word_file_path, pdf_file_path)
    print(f"Successfully converted {word_file_path} to {pdf_file_path}")

if __name__ == "__main__":
    word_file = input("Enter the path of the word file you want to convert: ")
    file_path = Path(word_file)
    if file_path.exists() and file_path.suffix == '.docx':
        convert_to_pdf(word_file)
    else:
        print("Invalid file path or file format")
