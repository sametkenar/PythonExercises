B = eval(input())

result = []
M, N = len(B), len(B[0])

for r in range(M):
    row = []
    for c in range(N):

        if B[r][c] == 'm':
            row.append('m')
            continue

        mine_count = 0
        if r > 0 and B[r-1][c] == 'm':  # north
            mine_count += 1

        if c < (N - 1) and B[r][c+1] == 'm':  # east
            mine_count += 1

        if r < (M - 1) and B[r+1][c] == 'm':     # south
            mine_count += 1

        if c > 0 and B[r][c-1] == 'm':      # west
            mine_count += 1

        row.append(mine_count)
    result.append(row)

print(result)