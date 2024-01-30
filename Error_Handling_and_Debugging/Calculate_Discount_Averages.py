def average_discount(list_of_changes):
    total = 0
    count = 0
    for change in list_of_changes:
        if change < 0:
            total += (-change) # to make it positive
            count += 1

        if count == 0:
            return 0 # No discounts, return 0 to avoid division by zero
        
        return round((total / count), 2) # rounding 2 digits after decimal point
    
def calculate_discount_averages(list_of_store_changes):
    averages = []

    for store_changes in list_of_store_changes:
        avg = average_discount(store_changes)
        averages.append(avg)
    
    return averages

# Example usage

list1 = [[-3.25, 4.5, 3.5], [-0.25, -2, -1, -1.5], [-4.25, -0.75, -2, 4.5]]
list2 = [[2.75, 3.25, -3.25], [2.5, 1.99, 1, 1, 0.5],
         [-0.25, -4.5, -2.25, -4, 2, 2], [-3, -2.5, -3, -1.99, -4.5]]
list3 = [[-0.75, 4, 2.25, 3.5, -1.25, 4.5],
         [-1.5, -2.99, 3.99, -0.25, -0.25, -2, 2.99, -4, -3.25],
         [1.25, 0.75, 0.5, 0.25, 1.5, 0.99],
         [0.25, 0.25, 0.75, 1.5, 2.75, 3, 2.25],
         [-3.25, 4.5, 4.99, 4.5, -1.99]]

print(calculate_discount_averages(list1))
print(calculate_discount_averages(list2))
print(calculate_discount_averages(list3))
