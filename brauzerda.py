from pywebio.input import file_upload
from pywebio.output import put_text, put_image
from pywebio import start_server
import cv2
import pytesseract
import numpy as np

# Matnni ajratib olish funksiyasi
def matnni_ajrat(rasm_bytes):
    # Tasvirni yuklash (bytes ko'rinishida)
    nparr = np.frombuffer(rasm_bytes, np.uint8)
    rasm = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # OCR orqali matnni ajratib olish
    matn = pytesseract.image_to_string(rasm, lang='uzb+eng+rus')
    return matn

# PyWebIO interfeys funksiyasi
def matnni_ajratish_xizmati():
    # Foydalanuvchidan rasm yuklashni so‘rash
    fayl = file_upload("Tasvirni yuklang:", accept="image/*")
    if not fayl:
        put_text("Hech qanday tasvir yuklanmadi!")
        return

    # Matnni ajratib olish
    matn = matnni_ajrat(fayl['content'])
    put_text("Tasvirdan ajratilgan matn:")
    put_text(matn)

# Serverni ishga tushirish
if __name__ == '__main__':
    start_server(matnni_ajratish_xizmati, port=8080)
