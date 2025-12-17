import os
import json
import time
import pyperclip


from emotion_detection import detect_emotion
from reply import suggested_reply

memory_file = "memory/inbox.json"

def load_memory():
    if not os.path.exists(memory_file):
        return []
    with open(memory_file,'r') as f:
        return json.load(f)
    


def run_assistant():
    print("Assistant Running....")
    print("Waiting for new message......")

    latest_index = -1

    while True:
        memory = load_memory()

        if len(memory) - 1 <= latest_index:
            time.sleep(1)
            continue

        latest_index = len(memory) - 1

        latest = memory[latest_index]
        if latest.get("sender") != "contact":
            time.sleep(1)
            continue

        message = latest["message"]

        print("Got New Message")
        print(message)

        emotion = detect_emotion()
        print(emotion)

        reply = suggested_reply(emotion)
        print("Suggested Reply: ", reply)
        pyperclip.copy(reply)

        time.sleep(1)

if __name__ == "__main__":
    run_assistant()