def is_divisor(number, divisor):
    return number % divisor == 0

def is_perfect(number):
    divisors_sum = 0
    for divisor in range(1, number):
        if is_divisor(number, divisor):
            divisors_sum += divisor
    return divisors_sum == number

# Example Usage
num = 28
print("Is", num, "a perfect number?", is_perfect(num)) #Output: True
print("Is", 6, "a perfect number?", is_perfect(6)) #Output: True
print("Is", 7, "a perfect number?", is_perfect(7)) #Output: True
print("Is", 28, "a perfect number?", is_perfect(28)) #Output: True
print("Is", 30, "a perfect number?", is_perfect(30)) #Output: True