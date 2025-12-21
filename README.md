# 📱 WhatsApp Automation Assistant (Python)

---------------------------------------------------------------------------------------------------

A simple Python-based WhatsApp automation project created for learning and demonstration purposes.
This project shows how automation, emotion detection, and rule-based replies can work together.

⚠️ This is NOT an official WhatsApp bot and does NOT use WhatsApp APIs.

-----------------------------------------------------------------------------------------------------
# 🚀 Quick Start 

1. Clone the repo  
2. Install dependencies
    pip install -r requirements.txt
4. Run `python main.py`  
5. Choose an option from the menu

------------------------------------------------------------------------------------------------------

# ✨ What This Project Does

This project has two main features:

✅ 1. Auto Reply Assistant (Clipboard-Based)

You copy a message (for example, from WhatsApp)

The program detects the emotion in the message

It generates a suggested reply

The reply is automatically copied back to your clipboard

You paste the reply manually

📌 This does not read WhatsApp messages automatically.

✅ 2. WhatsApp Bulk Messaging

Sends the same message to multiple contacts

Reads phone numbers from an Excel file

Uses WhatsApp Web automation

Adds delay between messages

📌 Intended only for testing and learning.

🧠 How Emotion Detection Works

Uses simple keyword matching

Detects emotions like:

Happy

Sad

Stressed

Excited

Neutral (default)

If no keywords are found, the message is marked as neutral

This keeps the project easy to understand and lightweight.

---------------------------------------------------------------------------------------------------

# 📁 Project Structure
whatsapp_automation/
│
├── main.py                 # Main menu and program control
├── assistant.py            # Clipboard auto-reply logic
├── bulk_message.py         # Bulk WhatsApp messaging
├── emotion_detection.py    # Emotion detection rules
├── reply.py                # Suggested replies
├── context_analyzer.py     # Message memory handling
├── README.md               # Project documentation
│
└── memory/
    └── inbox.json          # Saved message history


-------------------------------------------------------------------------------------------------


# 🛠 Requirements

Python 3.x

Google Chrome

WhatsApp Web account

Python Libraries
pip install pyperclip pywhatkit openpyxl

### Install dependencies
pip install -r requirements.txt

# Make sure you sign in to your WhatsApp Web atleast once before running Bulk Message.

-------------------------------------------------------------------------------------------------


# ▶️ How to Run
python main.py


You will see:

1. Whatsapp Bulk Message
2. Auto Reply Assistant
3. Run Both

📝 How to Use Auto Reply Assistant

Choose option 2

Copy any message text

The program:

Detects emotion

Generates a reply

Copies reply to clipboard

Paste the reply wherever you want

Stop anytime using Ctrl + C

📤 How to Use Bulk Messaging

Create an Excel file (.xlsx)

Put phone numbers in column A

Without country code

Choose option 1

Enter:

Excel file path

Message text

WhatsApp Web opens and sends messages


----------------------------------------------------------------------------------------------


# ⚠️ Important Warnings

🚫 WhatsApp Policy Warning

Uses browser automation (not official API)

May violate WhatsApp Terms of Service

Can result in temporary or permanent bans

Use a test WhatsApp account only.

----------------------------------------------------------------------------------------


# 🚫 Limitations

Not fully automatic

Clipboard-based reply system

Simple keyword emotion detection

No advanced error handling

Not production-ready

-------------------------------------------------------------------------------------------

# 🎓 Purpose of This Project

This project is meant for:

Learning Python automation

Understanding chatbot logic

College or academic projects

GitHub portfolio demonstrations

----------------------------------------------------------------------------------------------


# 🚀 Possible Improvements

Add AI/ML-based emotion detection

Add GUI

Improve error handling

Use official messaging APIs

Context-aware replies


-----------------------------------------------------------------------------------------------


# 📜 Disclaimer

This project is created only for educational purposes.
The author is not responsible for misuse, WhatsApp bans, or policy violations.

# ⭐ If You Like This Project

Feel free to ⭐ the repository and experiment with your own improvements.
