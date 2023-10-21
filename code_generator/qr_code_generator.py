from datetime import datetime
from dotenv import load_dotenv
import qrcode
import uuid

load_dotenv()

# Linked QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=15
)


def qr_encoder(qr_data):
    random_string = uuid.uuid4()
    file_name_id = str("My_QR_Code_") + str(f"{random_string}-") + datetime.now().strftime('%d%m%Y-%H%M%S') + str(
        ".png")
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'static\\{file_name_id}')
    return file_name_id


if __name__ == "__main__":
    data = input("Input your data: ")
    image = qr_encoder(data)
