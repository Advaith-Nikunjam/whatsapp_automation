import os
import json
import time
import pyperclip
from datetime import datetime

from emotion_detection import detect_emotion
from reply import suggested_reply

memory_file = "memory/inbox.json"

os.makedirs('memory',exist_ok = True)


if os.path.exists(memory_file):
    try:
        with open(memory_file,'r') as f:
            memory = json.load(f)
    except json.JSONDecodeError:
        memory = []
else:
    memory = []



def auto_reply():
    last_text = ""
    while True:
        current_text = pyperclip.paste()
        if not current_text or current_text == last_text:
            time.sleep(0.5)
            continue

        print("New Message: ")
        print(current_text)
        entry = {
            "time_stamp" : datetime.now().strftime("%Y-%m-%d %H:%M"),
            "message" : current_text,
            "sender" : "contact"
        }

        memory.append(entry)

        with open(memory_file,'w') as f:
            json.dump(memory,f,indent=2)

        emotion = detect_emotion(current_text)
        print("Detected emotion: ",emotion)
        reply = suggested_reply(emotion)
        print("Reply: ",reply)
        last_text = reply
        pyperclip.copy(reply)
        print("Replied copied! ")

        time.sleep(1)