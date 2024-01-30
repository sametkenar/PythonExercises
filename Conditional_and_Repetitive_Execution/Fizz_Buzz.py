n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz", end='\t')
    elif i % 3 == 0:
        print("Fizz", end='\t')
    elif i % 5 == 0:
        print("Buzz", end='\t')
    else:
        print(i, end='\t')