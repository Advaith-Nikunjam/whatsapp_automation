import json

memory_file = 'memory/inbox.json'

def load_memory():
    with open(memory_file,'r') as f:
        return json.load(f)
    
memory = load_memory()

def get_recent_context(n=5):
    memory = load_memory()
    return memory[-n:]

def latest_message():
    memory = load_memory()
    if not memory:
        return None
    return memory[-1]