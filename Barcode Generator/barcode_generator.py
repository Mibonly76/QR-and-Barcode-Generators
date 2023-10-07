import qrcode

# Linked QR Code

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=15
)

data = input("Input your data: ")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('Linked-Code.png')
