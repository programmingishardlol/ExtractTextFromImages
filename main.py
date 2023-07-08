# 'C:\Users\Vegas\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pytesseract.exe'
# go to https://github.com/UB-Mannheim/tesseract/wiki download tesseract first, then pip install pytesseract

from PIL import Image
from pytesseract import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'

class Imagereader:

    def __init__(self, os: OS):
        if os == OS.Mac:
            print("Running on Mac")

        if os == OS.Windows:
            windows_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = windows_path
            print("Running on Windows")

    def extract_text(self, image:str, lang:Language):
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang.value)
        return extracted_text

if __name__ == '__main__':
    ir = Imagereader(OS.Windows)
    text = ir.extract_text('images\shakespeare.png', lang=Language.ENG)
    processed_text = " ".join(text.split())
    print(processed_text)