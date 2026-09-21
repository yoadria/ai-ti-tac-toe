def get_state(board, player):
    return tuple(cell * player for cell in board)
