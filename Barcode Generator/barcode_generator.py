from barcode import EAN13
from datetime import datetime
file_name_id = str("My_QR_Code_") + datetime.now().strftime('%d%m%Y-%H%M%S')

number = input("Enter The Number: ")

if not number.isdigit():
    print("The entry value is not correct! It must be digits!")
    exit(200)
else:
    number = int(number)
    my_code = EAN13(number)
    my_code.save(f"{file_name_id}.png")
