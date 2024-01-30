debt = float(input())
total_money = debt * (1.02 ** 6)
monthly_payment = total_money / 6
print("{:.2f}".format(monthly_payment))