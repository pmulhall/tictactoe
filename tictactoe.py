"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math
import time

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
    """
    Returns player who has the next turn on a board.
    """
    qtyX = 0
    qtyO = 0

    for row in board:
        qtyX += row.count(X)
        qtyO += row.count(O)

    if qtyX > qtyO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available.add((i, j))

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newboard = deepcopy(board)
    (i,j) = action

    newboard[i][j] = player(board)

    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check rows
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    # check cols

    for j in range(3):
        col = []
        for i in range(3):
            col.insert(i, board[i][j])
        if col.count(X) == 3:
            return X
        if col.count(O) == 3:
            return O

    # check diags
    diag = []
    for d in range(3):
        diag.insert(d, board[d][d])
    if diag.count(X) == 3:
        return X
    if diag.count(O) == 3:
        return O

    diag = []
    diag.insert(0, board[0][2])
    diag.insert(0, board[1][1])
    diag.insert(0, board[2][0])
    if diag.count(X) == 3:
        return X
    if diag.count(O) == 3:
        return O


    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    else:
        blank = 0

        for row in board:
            blank += row.count(EMPTY)

        if blank == 0:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    current_player = player(board)

    start = time.time()
    alpha = -math.inf
    beta = math.inf

    if current_player == X:
        v = -math.inf

        for action in actions(board):
            k = minAB(result(board, action), alpha, beta)

            if k > v:
                v = k
                move = action
    else:
        v = math.inf

        for action in actions(board):
            k = maxAB(result(board, action), alpha, beta)

            if k < v:
                v = k
                move = action

    end=time.time()
    print("Processing Time:", end-start)

    return move

def minAB(board, alpha, beta):
    if terminal(board) == True:
        return utility(board)
    v = math.inf

    for action in actions(board):
        v = min(v, maxAB(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v

def maxAB(board, alpha, beta):
    if terminal(board) == True:
        return utility(board)
    v = -math.inf

    for action in actions(board):
        v = max(v, minAB(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v
