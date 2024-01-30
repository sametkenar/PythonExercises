def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count +=1
    return count

def winner(nazif, osman):
    N = divisors(nazif)
    O = divisors(osman)
    if N > O:
        return "Nazif"
    elif N < O:
        return "Osman"
    else: 
        return "Draw"

print(winner(120,144))
print(winner(191,190))
print(winner(4,121))


