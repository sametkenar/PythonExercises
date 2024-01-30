px = int(input())
py = int(input())
qx = int(input())
qy = int(input())

mx = (px + qx) / 2
my = (py + qy) / 2

rx = qx + (qx - px)
ry = qy + (qy - py)

print("{:.2f}".format(mx))
print("{:.2f}".format(my))
print("{:.2f}".format(rx))
print("{:.2f}".format(ry))