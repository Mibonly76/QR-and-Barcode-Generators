from barcode import EAN13
from datetime import datetime
file_name_id = str("My_BarCode_") + datetime.now().strftime('%d%m%Y-%H%M%S')

number = input("Enter The Number: ")

if not number.isdigit() or len(number) != 12:
    print("The entry value is not correct! It must be twelve digits!")
    exit(200)
else:
    my_code = EAN13(number)
    my_code.save(f"{file_name_id}")
