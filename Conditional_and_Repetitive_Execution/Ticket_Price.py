ages = eval(input())

total_price = 0

for age in ages:
    if 0 <= age <= 10:
        total_price += 30
    elif 11 <= age <= 25:
        total_price += 60
    elif 26 <= age <= 60:
        total_price += 90
    elif 60 < age:
        total_price += 50

print(total_price)