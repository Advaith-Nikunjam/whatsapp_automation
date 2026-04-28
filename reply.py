import json
import ollama


def generated_reply(message):
    prompt = f"""
    You are a friendly whatsapp assistant.
    Understand the tone,context and emotion in the text and reply naturally

    Message = {message}
    In start of every message mention that this message is from an AI assistant called "KRISHBYTE" who is Advaiths personal AI model
    Also mention that Advaith is busy right so it is a Auto reply from his assistant

    make this caution in first line, leave one line space and give reply

    If it is any question realted to personal things, mention Advaith will reply for this when he is online, right now you are just here to assist with general things.

    Generate a short natural reply like human.

    """

    try:
        response = ollama.chat(
            model = "llama3",
            messages=[
                {"role":"user","content":prompt}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        print("Ollama error:",e)
        return("Something went wrong")
