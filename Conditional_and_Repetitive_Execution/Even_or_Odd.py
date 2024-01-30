number = int(input())

if number % 2 == 0:
    if int(number/100) % 2 == 0:
        print("Even")
    else:
        print("Even Odd")
else:
    if int(number/100) % 2 != 0:
        print("Odd")
    else:
        print("Odd Even")