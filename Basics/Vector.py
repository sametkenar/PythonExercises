x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)

vector = (p1[0] + p2[0], p1[1] + p2[1])
translated_point = (vector[0] - p3[0], vector[1] - p3[1])

print(vector)
print(translated_point)