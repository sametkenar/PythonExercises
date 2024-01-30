G = eval(input())

M, N = len(G), len(G[0])    # dimensions of matrix
max_row_index = 0
max_row_sum = 0

for r in range(M):
    row_sum = 0
    for c in range(N):
        row_sum += G[r][c]

    if row_sum > max_row_sum:
        max_row_sum = row_sum
        max_row_index = r

max_row = G[max_row_index]
print(max_row)