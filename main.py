from bulk_message import bulk_message
from assistant import auto_reply


print("\n")
print("Hey Welcome!")
print("This project has 2 parts, ")
print("either you can send bulk messages to a number of contacts or whatsapp")
print("Or You can run a auto reply assistant which will help you reply to your whatsapp messages.")
print("-"*40)
print("\n"*2)
print("Choose the option you want")
print("1. Whatsapp Bulk Message reply")
print("2. Auto reply Assistant")
print("3> Run Both")
choice = int(input("Enter Your Choice - "))

if choice == 1:
    print("Running Whatsapp Bulk Messages!")
    excel_path = input("Enter The Location path address of your Excel Worksheet").strip().strip('"')
    print("Excel Location:",excel_path)
    message = input("Enter the message you want to send in whatsapp to these contacts")
    try:
        bulk_message(message,excel_path)
    except KeyboardInterrupt:
        print("Bulk message stoped")

elif choice == 2:
    print("Running reply assistant")
    print("You Can Now copy any text and reply for that text will be copied back on the clipboard")
    try:
        auto_reply()
    except KeyboardInterrupt:
        print("\n Auto Reply Stopped!")

elif choice == 3:
    print("Running Whatsapp Bulk Messages!")
    excel_path = input("Enter The Location path address of your Excel Worksheet").strip().strip('"')
    message = input("Enter the message you want to send in whatsapp to these contacts")
    try:
        bulk_message(message,excel_path)
    except KeyboardInterrupt:
        print("Bulk message stoped")


    print("Running reply assistant")
    print("You Can Now copy any text and reply for that text will be copied back on the clipboard")
    try:
        auto_reply()
    except KeyboardInterrupt:
        print("\n Auto Reply Stopped!")