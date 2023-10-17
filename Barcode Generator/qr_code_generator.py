import qrcode
from datetime import datetime
import shutil
# import os

# Linked QR Code

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=15
)
file_name_id = str("My_QR_Code_") + datetime.now().strftime('%d%m%Y-%H%M%S')

data = input("Input your data: ")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
image_name = f'{file_name_id}.png'
img.save(image_name)
dst_path = f"static\{image_name}"
shutil.move(image_name, dst_path)
