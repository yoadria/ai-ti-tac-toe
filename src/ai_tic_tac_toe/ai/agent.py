import random

def get_best_value(values):
    return max(values.values())

def get_best_action(values):
    best_value = get_best_value(values)

    for action, value in values.items():
        if value == best_value:
            return action
        
def get_best_actions(values):
    best_value = get_best_value(values)
    best_actions = []

    for action, value in values.items():
        if value == best_value:
            best_actions.append(action)

    return best_actions

def choose_action(values):
    best_actions = get_best_actions(values)
    return random.choice(best_actions)