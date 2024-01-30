def is_prime(number):       # helper function
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True
        
def find_first_non_prime(items):
    for item in items:
        if not is_prime(item):
            return item
    return False

print(find_first_non_prime([2,3,4,7]))
print(find_first_non_prime([2,3,5,7]))
print(find_first_non_prime([2,3,51,19]))