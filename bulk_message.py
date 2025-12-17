import pywhatkit
from openpyxl import workbook,load_workbook
import time
message1 = 'testing'
wb = load_workbook('Untitled spreadsheet (2).xlsx')
ws = wb.active
for i in range(1,ws.max_row+1):
    number = str(int(i))
    number = ws[f'A{i}'].value
    phone_number = f'+91{number}'
    #print(phone_number)

    pywhatkit.sendwhatmsg_instantly(
        phone_no = phone_number,



        message = message1,
        wait_time = 30,
        tab_close = False

        )
    time.sleep(30)