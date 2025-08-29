import sys
import time
import tictactoe as ttt

def print_board(board):
    """
    Nicely prints the Tic Tac Toe board to the terminal.
    """
    print("\nCurrent board:")
    for i in range(3):
        row = ""
        for j in range(3):
            cell = board[i][j] if board[i][j] != ttt.EMPTY else " "
            row += f" {cell} "
            if j < 2:
                row += "|"
        print(row)
        if i < 2:
            print("---+---+---")
    print()

def play_game():
    """
    Plays one game of Tic Tac Toe (user vs AI).
    """
    user = None
    board = ttt.initial_state()

    # Ask user to choose X or O
    while user not in [ttt.X, ttt.O]:
        choice = input("Do you want to play as X or O? ").upper()
        if choice in [ttt.X, ttt.O]:
            user = choice

    while True:
        print_board(board)

        if ttt.terminal(board):
            winner = ttt.winner(board)
            if winner is None:
                print("Game Over: Tie.")
            else:
                print(f"Game Over: {winner} wins!")
            break

        player = ttt.player(board)

        if user == player:
            # User's turn
            while True:
                try:
                    move = input(f"Your move ({user}). Enter row and column (e.g. 1 1 for top-left): ")
                    i, j = map(int, move.split())
                    i -= 1
                    j -= 1
                    if (i, j) in ttt.actions(board):
                        board = ttt.result(board, (i, j))
                        break
                    else:
                        print("Invalid move. Try again.")
                except Exception:
                    print("Please enter row and column as two numbers between 1 and 3.")
        else:
            # AI's turn
            print("Computer thinking...")
            time.sleep(1)
            move = ttt.minimax(board)
            print(f"Computer plays at {move[0] + 1} {move[1] + 1}")
            board = ttt.result(board, move)

def main():
    """
    Runs games in a loop until the player quits.
    """
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
