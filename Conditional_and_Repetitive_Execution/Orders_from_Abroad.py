N = int(input())
total_tax = 0

for _ in range(N):
    price = int(input())

    if 100 < price <= 1000:
        total_tax += price * (1/10)
    elif 1000 < price:
        total_tax += price * (2/10)

print (total_tax)
