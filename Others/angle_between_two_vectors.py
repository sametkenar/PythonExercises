from math import sqrt, acos

# Define two vectors that have 90deg (pi/2) between them

u = [1, 0, 0]
v = [0, 1, 0]
n = len(u)

if n != len(v):
    print("Sizes don't match!")

else:
    # Calculate dot product & norms
    dot_prod = u_norm_sum = v_norm_sum = 0
    for i in range(n):
        dot_prod += u[i] * v[i]
        u_norm_sum += u[i] ** 2
        v_norm_sum += v[i] ** 2

    u_norm = sqrt(u_norm_sum)
    v_norm = sqrt(v_norm_sum)

    theta = acos(dot_prod / u_norm * v_norm)
    
    print("angle between u and v is: ", theta)