"""
Tic Tac Toe Player
"""
import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """ return next player """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    elif o_count > x_count:
        return X
    elif o_count == x_count == 0:
        return X


def actions(board):
    """
    Return all possible actions
    """
    empty_cell = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cell.add((i, j))
    return empty_cell


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action
    if board[i][j] is not None:
        raise ValueError("Invalid action: cell is not empty.")

    board[i][j] = player(board)
    return board





def winner(board):
    """
    Return if game is over and somebody is won
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None


def terminal(board):
    """
    Return True if no one win
    """
    empty_count = sum(row.count(EMPTY) for row in board)
    if winner(board) or empty_count == 0:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    state = winner(board)
    if state == X:
        return 1
    elif state == O:
        return -1
    else:
        return 0


max_score = 1000
min_score = -1000
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        raise ValueError("Game end!")  # Если игра завершена, мы не можем сделать ход.

    current_player = player(board)


    if current_player == X:
        max_eval = min_score
        best_move = None
        for action in actions(board):
            new_board = result(board, action)  # Сделать ход
            eval_value = utility(new_board)  # Получить оценку для следующего хода
            if eval_value > max_eval:
                max_eval = eval_value
                best_move = action
        if best_move is None:  # Если не найден лучший ход, возвращаем последний возможный ход
            best_move = actions(board).pop()
        return best_move

    elif current_player == O:
        min_eval = max_score
        best_move = None
        for action in actions(board):
            new_board = result(board, action)  # Сделать ход
            eval_value = utility(new_board)  # Получить оценку для следующего хода
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = action
        if best_move is None:  # Если не найден лучший ход, возвращаем последний возможный ход
            best_move = actions(board).pop()
        return best_move







