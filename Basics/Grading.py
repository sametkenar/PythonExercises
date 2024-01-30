ass1 = int(input())
ass2 = int(input())
ass3 = int(input())
ass4 = int(input())
ass5 = int(input())

grades = [ass1, ass2, ass3, ass4, ass5]
grades.remove(min(grades))

total = (sum(grades) * 5) / 40
print(total)