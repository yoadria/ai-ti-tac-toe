def new_board() -> list:
    return [0,0,0,0,0,0,0,0,0] 

def show_board(board: list):
    for row in range(3):
        for column in range(3):
            index = row * 3 + column
            print(board[index], end=" ")
        print()

def is_valid_move(board: list, position: int) -> bool:
    """Determinamos si el movimiento es valido """
    if position >= 0 and position <= 8:
        if board[position] == 0:
            return True
    
    return False

def make_move(board: list, position: int, player: int) -> list:
    """En esta funcion no comprobamos si la posicion es valida o no,
    solo nos encargaremos de realizar el movimiento."""
    
    board[position] = player
    return board

def get_available_moves(board: list) -> list:
    availables = []
    for position, value in enumerate(board):
        if value == 0:
            availables.append(position)
    
    return availables
            
def check_winner(board: list) -> int:
    
    results = [
        sum(board[0:3]),
        sum(board[3:6]),
        sum(board[6:9]),

        sum(board[i] for i in (0, 3, 6)),
        sum(board[i] for i in (1, 4, 7)),
        sum(board[i] for i in (2, 5, 8)),

        sum(board[i] for i in (0, 4, 8)),
        sum(board[i] for i in (2, 4, 6)),
    ]

    for result in results:
        if result == 3 or result == -3:
            return result

    return 0

def is_draw(board: list) -> bool:
    draw = check_winner(board)
    
    if draw == 0:
        return True
    return False