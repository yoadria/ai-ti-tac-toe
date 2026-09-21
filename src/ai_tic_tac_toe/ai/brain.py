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