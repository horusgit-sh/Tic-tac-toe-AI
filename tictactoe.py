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
    return X


def actions(board):
    """
    Return all possible actions
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = [row[:] for row in board]  # Копируем доску
    i, j = action
    new_board[i][j] = player(board)
    return new_board





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
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


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



def minimax(board, depth=10):
    """
   Return best move
    """

    def maximize(board, depth):
        if terminal(board) or depth == 0:
            return utility(board), None

        best_move = None
        best_eval = float('-inf')

        for action in actions(board):
            new_board = result(board, action)
            eval_value, _ = minimize(new_board, depth - 1)

            if eval_value > best_eval:
                best_eval = eval_value
                best_move = action

        return best_eval, best_move

    def minimize(board, depth):

        if terminal(board) or depth == 0:
            return utility(board), None

        best_move = None
        best_eval = float('inf')

        for action in actions(board):
            new_board = result(board, action)
            eval_value, _ = maximize(new_board, depth - 1)

            if eval_value < best_eval:
                best_eval = eval_value
                best_move = action

        return best_eval, best_move


    current_player = player(board)
    if current_player == X:
        _, best_move = maximize(board, depth)
    elif current_player == O:
        _, best_move = minimize(board, depth)

    return best_move






