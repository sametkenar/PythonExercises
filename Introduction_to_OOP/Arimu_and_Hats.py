def buy_hats(hat_costs, money):
    hat_costs.sort()        # Sort the list of hat costs in ascending order
    total_hats = 0

    for cost in hat_costs:
        if cost <= money:
            money -= cost
            total_hats += 1
        else:
            break
    
    return total_hats

# Example Usage
hat_prices = [10, 7, 5, 15, 20]
arimus_money = 25
max_hats = buy_hats(hat_prices, arimus_money)
print("Maximum number of hats Arimu an buy: ", max_hats)

print(buy_hats([12, 3, 7, 5, 4, 8], 12))
print(buy_hats([4, 3, 6, 2, 5, 5], 27))

