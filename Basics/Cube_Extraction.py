m = int(input())
n = int(input())

# extracting the smaller cube adds 2 new surface areas to the total surface area of original cube.
res = (m ** 2) * 6 + (n ** 2) * 2
print(res)