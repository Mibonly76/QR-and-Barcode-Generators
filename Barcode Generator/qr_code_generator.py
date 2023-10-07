import qrcode
from datetime import datetime

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
img.save(f'{file_name_id}.png')
