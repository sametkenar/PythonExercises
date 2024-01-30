def has_real_roots(a,b,c):
    delta = (b**2) - (4 * a * c)
    return delta >= 0 


print(has_real_roots(1,-2,4))