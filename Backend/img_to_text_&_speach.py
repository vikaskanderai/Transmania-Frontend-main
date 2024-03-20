# pip install pytesseract opencv-python pywin32
import cv2
import pytesseract
from win32com.client import Dispatch

# Specify Tesseract executable path (replace 'path_to_tesseract' with the actual path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\vikas.LAPTOP-RRF59END\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load image
img_path = 'C:\\Users\\vikas.LAPTOP-RRF59END\\OneDrive\\Desktop\\quote2.png'
img = cv2.imread(img_path)

# Perform OCR using pytesseract
text = pytesseract.image_to_string(img, lang='kan')

# Save recognized text to a file
with open("img_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
print(text)

