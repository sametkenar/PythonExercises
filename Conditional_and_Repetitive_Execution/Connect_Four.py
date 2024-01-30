n = int(input())
board = [input() for _ in range(n)]

# Check rows for a winner
for row in board:
    if 'RRRR' in row or 'YYYY' in row:
        print("yes")
        exit()

# Check columns for a winner
for j in range(n):
    column = ''.join(board[i][j] for i in range(n))
    if 'RRRR' in column or 'YYYY' in column:
        print("yes")
        exit()

# Check diagonals for a winner
for i in range(n - 3):
    for j in range(n - 3):
        diagonal1 = ''.join(board[i+k][j+k] for k in range(4))
        diagonal2 = ''.join(board[i+3-k][j+k] for k in range(4))
        if 'RRRR' in diagonal1 or 'YYYY' in diagonal1 or 'RRRR' in diagonal2 or 'YYYY' in diagonal2:
            print("yes")
            exit()

print("no")
