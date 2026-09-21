import json
from pathlib import Path

BRAIN_PATH = Path(__file__).resolve().parents[3]/"data"/"brain.json"

brain = {}

def get_value(state, action):
    """obtengo el valor de una jugada, si no existe obtengo 0.0"""
    return brain.get((state, action), 0.0)

def set_value(state, action, value):
    """guardo el valor de una jugada"""
    brain[(state, action)] = value

def get_action_values(state, actions):
    values = {}

    for action in actions:
        value = get_value(state, action)
        values[action] = value
    return values

def load_brain():
    
    global brain
    
    if not BRAIN_PATH.exists():
        brain = {}
        return brain
    
    with open(BRAIN_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        
    brain = {}
    
    for item in data:
        state = tuple(item["state"])
        action = item["action"]
        value = item["value"]
        
        brain[(state, action)] = value
        
    return brain

def save_brain():
    
    BRAIN_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    data = []
    
    for (state, action), value in brain.items():
        data.append(
            {
                "state": list(state),
                "action": action,
                "value": value,
            }
        )
        
    with open(BRAIN_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)