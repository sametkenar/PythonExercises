def countdown(money_left, payments):
    months_left = 0

    for payment in payments:
        money_left -= payment
        if money_left <= 0:
            return months_left
        months_left +=1

    return months_left

# Example
initial_money = 10000
monthly_payments = [3000, 2500, 2000, 3500]
months_until_bankrupt = countdown(initial_money, monthly_payments)
print("Months until baknruptcy: ", months_until_bankrupt)

print(countdown(2000,[2900,1000,400,23000]))
print(countdown(12500,[7000, 4500, 750, 150, 7100, 1000]))