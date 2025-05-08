import pytesseract
from PIL import Image
# Rasmni ochamiz
image = Image.open("a-1704914000276-2x.jpg")

# Matnni chiqaramiz
text = pytesseract.image_to_string(image)
print(text)
