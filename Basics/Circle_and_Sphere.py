from math import pi

r = float(input())

circle_area = pi * (r ** 2)
sphere_volume = (4/3) * pi * (r**3)

print("circle area: {:.2f}".format(circle_area))
print("sphere volume: {:.2f}".format(sphere_volume))