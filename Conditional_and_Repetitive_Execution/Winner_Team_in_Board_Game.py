B = eval(input())

N = len(B)  # dimension of the board
result = 0

i = 0
while i < N:
    j = 0
    while j < N:
        if B[i][j] < 0:
            result += (- B[i][j])   # to make it positive
        j += 1
    i += 1

print(result)