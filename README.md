# 📱 NLP-Based WhatsApp Automation Assistant (Python)

---

An **NLP-based WhatsApp automation project** built using Python for learning and demonstration purposes.
This project combines **automation**, **rule-based natural language processing (NLP)**, and **emotion-aware response generation**.

⚠️ **Important:** This is **NOT an official WhatsApp bot** and does **NOT** use WhatsApp’s official APIs.

---

## 🚀 Overview

The goal of this project is to demonstrate how:

* Natural language input can be analyzed
* Emotions can be inferred from text
* Automated yet *context-aware* replies can be generated
* Messaging workflows can be automated responsibly for learning purposes

This project is **not production-ready** and is intended **only for educational use**.

---

## ✨ Features

### ✅ 1. NLP-Based Auto Reply Assistant (Clipboard-Based)

* Copy any incoming message text (e.g., from WhatsApp)
* The system:

  * Analyzes the text
  * Detects the **emotion** using rule-based NLP
  * Generates a **contextual reply**
* The reply is automatically copied back to your clipboard
* Paste the reply manually wherever required

📌 This assistant **does not read WhatsApp messages directly**.

---

### ✅ 2. WhatsApp Bulk Messaging Automation

* Sends the same message to multiple contacts
* Reads phone numbers from an Excel file (`.xlsx`)
* Uses WhatsApp Web automation
* Introduces random delays between messages to reduce spam-like behavior

📌 Intended strictly for **testing and learning purposes**.

---

## 🧠 NLP & Emotion Detection Logic

This project uses **rule-based NLP**, not machine learning.

### Emotion Detection:

* Keyword matching approach
* Supported emotions:

  * Happy
  * Sad
  * Stressed
  * Excited
  * Neutral (default)

If no emotion-related keywords are found, the message is marked as **Neutral**.

This design keeps the project:

* Lightweight
* Easy to understand
* Beginner-friendly

---

## 📁 Project Structure

```
whatsapp_automation/
│
├── main.py                 
├── assistant.py            
├── bulk_message.py         
├── emotion_detection.py    
├── reply.py                
├── context_analyzer.py     
├── requirements.txt
├── README.md
│
└── memory/
    └── inbox.json          
```

---

## 🛠 Requirements

* Python 3.x
* Google Chrome
* WhatsApp Web account

### Python Libraries

```
pip install pyperclip pywhatkit openpyxl
```

or

```
pip install -r requirements.txt
```

📌 Make sure you are logged into **WhatsApp Web at least once** before running bulk messaging.

---

## ▶️ How to Run

```
python main.py
```

You will see the following options:

1. WhatsApp Bulk Messaging
2. NLP Auto Reply Assistant
3. Run Both

---

## 📝 How to Use the Auto Reply Assistant

1. Choose option **2**
2. Copy any message text
3. The system will:

   * Detect emotion
   * Generate a suggested reply
   * Copy it to the clipboard
4. Paste the reply manually

Stop anytime using **Ctrl + C**

---

## 📤 How to Use Bulk Messaging

1. Create an Excel file (`.xlsx`)
2. Add phone numbers in **Column A** (without country code)
3. Choose option **1**
4. Enter:

   * Excel file path
   * Message text
5. WhatsApp Web opens and sends messages automatically

---

## ⚠️ Warnings & Disclaimer

🚫 **WhatsApp Policy Warning**

* Uses browser automation (not official APIs)
* May violate WhatsApp Terms of Service
* Can result in temporary or permanent bans

⚠️ **Use a test WhatsApp account only**

---

## 🚫 Limitations

* Not fully automated
* Clipboard-based reply system
* Simple keyword-based NLP
* No ML or deep learning models
* Minimal error handling
* Not production-ready

---

## 🎓 Purpose of This Project

This project is intended for:

* Learning Python automation
* Understanding basic NLP concepts
* Exploring chatbot logic
* College / academic submissions
* GitHub portfolio demonstrations

---

## 🚀 Possible Improvements

* ML-based or transformer-based emotion detection
* Context-aware multi-turn replies
* GUI or web interface
* Better memory handling
* Official messaging APIs
* Improved NLP preprocessing

---

## 📜 Disclaimer

This project is created **strictly for educational purposes**.
The author is **not responsible** for misuse, WhatsApp bans, or policy violations.

---

⭐ If you find this project useful, feel free to star the repository and build on top of it!
