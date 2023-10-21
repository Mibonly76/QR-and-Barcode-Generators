from barcode import EAN13
from datetime import datetime
import uuid

random_string = uuid.uuid4()
file_name_id = str("My_BarCode_") + str(f"{random_string}-") + datetime.now().strftime('%d%m%Y-%H%M%S')

number = input("Enter The Number: ")

if not number.isdigit() or len(number) != 13:
    print("The entry value is not correct! It must be thirteen digits!")
    exit(200)
else:
    my_code = EAN13(number)
    my_code.save(f"{file_name_id}")
