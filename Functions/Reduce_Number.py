def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reduce_number(number):
    while number >= 10:
        number = sum_of_digits(number)

    return number

# Example Usage

num = 325565
reduced_num = reduce_number(num)

print("Reduced number: ", reduced_num) # Output: 8

print(reduce_number(589564123))
print(reduce_number(19999999999999))