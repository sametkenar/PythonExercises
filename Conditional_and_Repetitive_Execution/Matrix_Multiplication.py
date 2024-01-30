matrix1 = eval(input())
matrix2 = eval(input())

# Do not change the lines above

first_dimension_matrix1 = len(matrix1)
second_dimension_matrix2 = len(matrix2[0])
mutual_dimension = len(matrix2) # or it could be len(matrix1[0])
new_generated_matrix = [0] * first_dimension_matrix1
for i in range(first_dimension_matrix1):
    new_generated_matrix[i] = [0] * second_dimension_matrix2
for row in range(first_dimension_matrix1):
    for column in range(second_dimension_matrix2):
        for i in range(mutual_dimension):
            new_generated_matrix[row][column] += matrix1[row][i] * matrix2[i][column]

print(new_generated_matrix)
