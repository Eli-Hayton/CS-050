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
    """
    Returns player who has the next turn on a board.
    """

    #Row is the rows in the array board ie the [Empty Empty Empty]
    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board) # gets # of o's and x's in board

    # X always goes first so
    if (xCount <= oCount):
        return X
    else :
        return O
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j)) #add cords of empty places to the set
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Illegal Move")
    
    i, j = action
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    # Check if any line has same player
    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    turn = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state)
        v = -math.inf
        for a in actions(state):
            v = max(v, min_value(result(state, a)))
        return v

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = math.inf
        for a in actions(state):
            v = min(v, max_value(result(state, a)))
        return v

    best_action = None

    if turn == X:
        best_val = -math.inf
        for a in actions(board):
            move_val = min_value(result(board, a))
            if move_val > best_val:
                best_val = move_val
                best_action = a
    else:
        best_val = math.inf
        for a in actions(board):
            move_val = max_value(result(board, a))
            if move_val < best_val:
                best_val = move_val
                best_action = a

    return best_action
