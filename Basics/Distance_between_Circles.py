from math import sqrt

x_1 = int(input())
y_1 = int(input())
radius_1 = int(input())

x_2 = int(input())
y_2 = int(input())
radius_2 = int(input())

a = (x_2 - x_1) ** 2
b = (y_2 - y_1) ** 2

distance = sqrt(a + b) - (radius_1 + radius_2)

print("{:.2f}".format(distance))