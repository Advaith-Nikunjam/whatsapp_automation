# import pyperclip
# import time
# import os
# import json
# from datetime import datetime



# memory_file = 'memory/inbox.json'
# os.makedirs('memory',exist_ok = True)


# if os.path.exists(memory_file):
#     try:
#         with open(memory_file,'r') as f:
#             memory = json.load(f)
#     except json.JSONDecodeError:
#         memory = []
# else:
#     memory = []

# last_text = ""

# while True:
#     current_text = pyperclip.paste()
#     if current_text and current_text != last_text:
#         last_text = current_text
#         print("New clipboard content detected!")
#         entry = {
#             "time_stamp" : datetime.now().strftime("%Y-%m-%d %H:%M"),
#             "message" : current_text,
#             "sender" : "contact"
#         }

#         memory.append(entry)

#         with open(memory_file,'w') as f:
#             json.dump(memory,f,indent=2)

        
#         print('saved message')
#         print(current_text)
#         print("-"*40)
    
#     time.sleep(1)