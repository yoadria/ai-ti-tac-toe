from . import board


def start_game():
    """Crea el tablero e inicia el juego."""
    game_board = board.new_board()
    player = board.X

    return game_board, player


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


def turn(game_board: list, player: int):
    """Ejecuta un turno completo."""

    play_player(game_board, player)

    board.show_board(game_board)

    winner = board.check_winner(game_board)

    if winner != board.EMPTY:
        return winner

    if not board.get_available_moves(game_board):
        return "draw"

    return None


def game():
    """Controla una partida completa."""

    game_board, player = start_game()

    board.show_board(game_board)

    while True:
        result = turn(game_board, player)

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


if __name__ == "__main__":
    game()