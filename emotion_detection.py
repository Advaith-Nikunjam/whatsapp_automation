#from main import latest_message

EMOTION_KEYWORDS = {
    "happy": [
        "haha", "lol", "😂", "😄", "😊", "good", "great", "nice"
    ],
    "stressed": [
        "stress", "tension", "worried", "scared", "exam", "pressure"
    ],
    "sad": [
        "sad", "bad", "upset", "cry", "hurt", "lonely"
    ],
    "excited": [
        "excited", "yay", "awesome", "can't wait", "🔥", "😍"
    ]
}

def detect_emotion(text):

    if not text:
        return "neutral"
    
    text = text.lower()

    score = {emotion:0 for emotion in EMOTION_KEYWORDS}

    for emotion, keyword in EMOTION_KEYWORDS.items():
        for word in keyword:
            if word in text:
                score[emotion] +=1

    
    detected = max(score,key=score.get)

    if score[detected] == 0:
        return 'neutral'
    
    return detected