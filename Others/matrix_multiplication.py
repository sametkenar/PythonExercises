A = [[-2,3,5,-1], [0,3,10,-7], [11,0,0,-8]]
B = [[2,1], [-1,1], [0,4], [8,0]]

# C = A*B

# Create a result matrix with entries filled with 0 (zeros)

C = []
for i in range(len(A)):
    C += [[0] * len(B[0])] # This is done to overcome the aliasing problem

for i in range(len(C)):
    for j in range(len(C[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k]*B[k][j]

print(C)