EMPTY = 0
X = 1
O = -1


def new_board() -> list:
    return [EMPTY] * 9 

def show_board(board: list):
    symbols = {
        EMPTY: " ",
        X: "X",
        O: "O",
    }
    
    for row in range(3):
        start = row *3
        print(
            f" {symbols[board[start]]} "
            f"| {symbols[board[start + 1]]} "
            f"| {symbols[board[start + 2]]} "
        )
        
        if row < 2:
            print("---+---+---")

def is_valid_move(board: list, position: int) -> bool:
    """Determinamos si el movimiento es valido """
    if position >= 0 and position <= 8:
        if board[position] == EMPTY:
            return True
    
    return False

def make_move(board: list, position: int, player: int) -> list:
    """En esta funcion no comprobamos si la posicion es valida o no,
    solo nos encargaremos de realizar el movimiento."""
    
    board[position] = player
    

def get_available_moves(board: list) -> list:
    availables = []
    for position, value in enumerate(board):
        if value == EMPTY:
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
        if result == 3:
            return X
        if result == -3:
            return O

    return EMPTY
