from context_analyzer import get_recent_context,latest_message
from emotion_detection import detect_emotion


class history:
    print("Recent message!")

    for msg in get_recent_context(3):
        print(msg)


    print('lastest Message')
    print(latest_message())

class emotion:
    emotion_det = detect_emotion()
    print("Detected Emotion: ",emotion_det)