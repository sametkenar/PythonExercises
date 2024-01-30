def find_zero(numbers):
    index_of_zero = -1
    index_counter = -1

    try:
        for number in numbers:
            index_counter += 1
            temporary = 32/number # Apply division to catch ZeroDivisionError exception.
    except ZeroDivisionError:
        index_of_zero = index_counter
    
    return index_of_zero

print(find_zero([1,2,3,4,5]))
print(find_zero([123,35,0,46,2567]))
print(find_zero([0,1,0,1,1,0]))

