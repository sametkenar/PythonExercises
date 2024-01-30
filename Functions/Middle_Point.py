def middle_point(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2
    middle_point = (middle_x , middle_y)
    return middle_point

# Example Usage
point1 = (-4.0, 2.0)
point2 = (3.0, -4.0)
mid_point = middle_point(point1, point2)
print("Middle point: ", mid_point)
