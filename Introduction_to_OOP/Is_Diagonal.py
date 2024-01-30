def is_diagonal(matrix):
    n = len(matrix)

    for i in range(n):
        zeros = matrix[i].count(0)
        if(zeros != n-1 or matrix[i][i] == 0):
            return False
    
    return True

print(is_diagonal([[1,0,0],[0,1,0],[0,0,1]]))
print(is_diagonal([[1,1,1],[2,4,0],[3,3,3]]))


