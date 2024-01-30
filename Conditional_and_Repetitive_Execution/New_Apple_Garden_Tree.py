G = eval(input())   # I DID NOT DO IT

M, N = len(G), len(G[0])    # dimensions of matrix

max_col_idx = 0
max_col_sum = 0


for j in range(N):
    col_sum = 0
    for i in range(M):
        col_sum += G[i][j]

    if col_sum > max_col_sum:
        max_col_sum = col_sum
        max_col_idx = j

max_col = G[max_col_idx]

print("Column", max_col, "produces the highest count of apples.")
# [[30, 40, 20, 50], [60, 20, 40, 10], [50, 30, 70, 60], [30, 40, 40, 20]]
