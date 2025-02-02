def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all([spot == player for spot in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def get_player_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def update_board(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Cell already taken. Try again.")
        return False

def tic_tac_toe():
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_move(current_player)
        if update_board(board, row, col, current_player):
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()