from . import board
from ..ai import state
from ..ai import brain
from ..ai import agent
from ..ai import learning

def start_game():
    """Crea el tablero e inicia el juego."""
    game_board = board.new_board()
    player = board.X

    return game_board, player

def turn(game_board: list, player: int, history: list):
    """Ejecuta un turno completo."""
    
    current_state = state.get_state(game_board, player)

    if player == board.X:
        action = play_player(game_board, player)
    else:
        action = play_ai(game_board, player)
        
    history.append(
        (current_state, action, player)
    )

    board.show_board(game_board)

    winner = board.check_winner(game_board)

    if winner != board.EMPTY:
        return winner

    if not board.get_available_moves(game_board):
        return "draw"

    return None


def game():
    """Controla una partida completa."""
    
    brain.load_brain()
    
    game_board, player = start_game()
    
    history = []
    
    board.show_board(game_board)

    while True:
        result = turn(game_board, player, history)

        if result == board.X:
            print("Ha ganado X")
            break

        if result == board.O:
            print("Ha ganado O")
            break

        if result == "draw":
            print("Empate")
            break

        player *= -1
        
    learning.learn_from_game(history, result)
    brain.save_brain()

def play_player(game_board: list, player: int):
    """Jugada de un jugador."""
    position = int(
        input(f"Jugador {player}, elige una posicion (0-8): ")
    )

    while not board.is_valid_move(game_board, position):
        position = int(
            input("No es una posicion valida. Elige una entre (0-8): ")
        )

    board.make_move(game_board, position, player)

    return position

def play_ai(game_board: list, player: int):
    """Realiza una jugada de la IA."""

    current_state = state.get_state(game_board, player)

    actions = board.get_available_moves(game_board)

    values = brain.get_action_values(current_state, actions)

    action = agent.choose_action(values)

    board.make_move(game_board, action, player)
    
    return action

if __name__ == "__main__":
    game()