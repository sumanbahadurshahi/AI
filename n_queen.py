class Solution:
    # Function to check if placing a queen at (row, col) is safe
    def isSafe(self, board, row, col, n):
        # Check left in the same row
        for j in range(col):
            if board[row][j] == 'Q':
                return False

        # Check upward in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True  # Safe to place a queen here

    # Backtracking function to try placing queens row by row
    def nQueens(self, board, row, n, ans):
        # If all queens are placed successfully
        if row == n:
            ans.append(board[:])  # Add the current board configuration to result
            return

        # Try placing a queen in all columns of the current row
        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row] = board[row][:j] + 'Q' + board[row][j+1:]  # Place the queen
                self.nQueens(board, row + 1, n, ans)                  # Recurse to next row
                board[row] = board[row][:j] + '.' + board[row][j+1:]  # Backtrack

    # Main function to initiate the N-Queens solver
    def solveNQueens(self, n):
        board = ['.' * n for _ in range(n)]  # Initialize an n x n empty board
        ans = []                             # List to store all valid boards

        self.nQueens(board, 0, n, ans)       # Start backtracking from row 0

        return ans                           # Return all solutions


# Main driver code (like your main() in C++)
sol = Solution()
n = 4  # You can change n to try different sizes

result = sol.solveNQueens(n)  # Get all valid solutions

# Print the result
# Loop through each valid board in the result
for board in result:
    # Print each row of the board
    for row in board:
        print(row)  # Example: "..Q."
    # After one board is printed, separate it visually
    print("----")
