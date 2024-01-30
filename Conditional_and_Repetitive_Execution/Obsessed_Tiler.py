T = eval(input())

N = len(T)

result = True

for i in range(N):
    if not result:
        break

    for j in range(N):
        if T[i][j] != T[j][i]:
            result = False
            break

print(result)