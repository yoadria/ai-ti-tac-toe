from . import brain


LEARNING_RATE = 0.1

WIN_REWARD = 1.0
LOSS_REWARD = -1.0
DRAW_REWARD = 0.0


def learn_from_game(history, result):
    """Aprende de todas las jugadas realizadas durante una partida."""

    for state, action, player in history:

        if result == "draw":
            reward = DRAW_REWARD

        elif result == player:
            reward = WIN_REWARD

        else:
            reward = LOSS_REWARD

        old_value = brain.get_value(state, action)

        new_value = old_value + LEARNING_RATE * (
            reward - old_value
        )

        brain.set_value(state, action, new_value)