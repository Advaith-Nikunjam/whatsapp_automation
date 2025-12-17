import json
from emotion_detection import detect_emotion

def suggested_reply(emotion):
    replies = {
        "stressed": "Don’t worry, you’ve prepared well. You’ll do great ❤️",
        "happy": "Haha 😄 that’s nice!",
        "sad": "I’m here for you. Tell me what happened 💙",
        "excited": "That’s awesome! 🔥",
        "neutral": "Hmm okay 🙂"
    }
    return replies.get(emotion, "Hmm😊")