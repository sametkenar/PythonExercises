def is_even(number):
    if(number == 1):
        return False
    elif(number == 0):
        return True
    else:
        return is_even(number - 2)

print(is_even(122))
print(is_even(55))
print(is_even(1))
print(is_even(0))