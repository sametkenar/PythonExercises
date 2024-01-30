# Define the vectors (as lists)
u = [1, 2, 4, 10]
v = [10, 4, 2, 1]
n = len(u)
dot_prod = 0

if n != len(v): print("Sizes don't match!")
else:
    for i in range(n):
        dot_prod += u[i] * v[i]
    print("u . v is: ", dot_prod)