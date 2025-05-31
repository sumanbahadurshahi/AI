# Initialize a 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

# Check for a winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != ' ' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return ' '

# Check if the board is full (draw)
def is_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Try to win or block
def try_win_or_block(symbol):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = symbol
                if check_winner() == symbol:
                    return True
                board[i][j] = ' '  # Undo move
    return False

# AI move logic
def ai_move():
    # 1. Try to win
    if try_win_or_block('X'):
        return
    # 2. Try to block player
    if try_win_or_block('X'):
        return
    # 3. Take center
    if board[1][1] == ' ':
        board[1][1] = 'X'
        return
    # 4. Take any corner
    for r, c in [(0,0), (0,2), (2,0), (2,2)]:
        if board[r][c] == ' ':
            board[r][c] = 'X'
            return
    # 5. Take any side
    for r, c in [(0,1), (1,0), (1,2), (2,1)]:
        if board[r][c] == ' ':
            board[r][c] = 'X'
            return

def player_move(): #input() gets something like "1 2"

                   #split() turns it into ['1', '2']
    while True:
        try:
            print("Enter your move (row and column from 0 to 2): ", end='')
            row, col = map(int, input().split())

            if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Invalid move. Try again.\n")

        except:
            print("Invalid input. Please enter two numbers (0 to 2).\n")




def main():
    print("Welcome to Tic Tac Toe! AI (X) vs You (O)")
    print_board()

    while True:
        ai_move()
        print("\nAI's Move:")
        print_board()
        if check_winner() == 'X':
            print("AI wins!")
            break
        if is_full():
            print("It's a draw!")
            break

        player_move()
        print("\nYour Move:")
        print_board()
        if check_winner() == 'O':
            print("You win!")
            break
        if is_full():
            print("It's a draw!")
            break


main()
