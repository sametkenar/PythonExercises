# try with different boards
board = [ ["_", "_", "q", "_"]
        , ["q", "_", "_", "_"]
        , ["_", "_", "_", "q"]
        , ["_", "q", "_", "_"]
        ]

length = len(board)

valid = True

for i in range(length):
    if not valid:
        break
    queens_in_row = 0 #each row should have exactly one queen
    for j in range(length):
        if not valid:
            break
        elif board[i][j] == "q":
            if queens_in_row != 0: #two queens in the same row
                valid = False
            #check squares in the j'th column of the previous rows
            for k in range(i):
                if not valid:
                    break
                elif board[k][j] == "q": #two queens in the same column
                    valid = False
                elif j + k - i >= 0 and board[k][j + k - i] == "q": #diagonal
                    valid = False
                elif j + i - k < length and board[k][j + i - k] == "q":
                    valid = False
            queens_in_row = 1
    if queens_in_row != 1: #empty row
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")