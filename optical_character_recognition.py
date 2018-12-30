import cv2
import pytesseract
from PIL import Image
#check for image and  proper installation of libraries and  
def main():
    path="C:/Users/ANKIT/Desktop/idd.jpg"
    image=cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    text = pytesseract.image_to_string(Image.open("C:/Users/ANKIT/Desktop/idd.jpg"))
    print("OCR Text is " + text)
try:
    main()
except Exception as e:
    print(e.args)
    print(e.__cause__)