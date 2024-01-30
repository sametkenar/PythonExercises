def total_price(prices, l, r):
    total_cost = 0
    for i in range(l-1, r-1):
        total_cost += prices[i]
    
    return total_cost

print(total_price([1,5,2,6,12,5,23,15],2,6))
print(total_price([7,7,7,5,6,3,5,7,8],1,9))

