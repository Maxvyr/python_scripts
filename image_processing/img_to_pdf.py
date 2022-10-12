import img2pdf
from PIL import Image
import os
  
# storing image path
img_path = "img_waifu.jpeg"
  
# storing pdf path
pdf_path = "img_waifu.pdf"
  
print("Start converting ...")
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()  
file.close()
  
print("convert to pdf finish ✅")