n = int(input())
s = ""

for i in range(7, -1 ,-1):
    if n >= 2**i:
        s += "1"
        n -= 2**i
    else:
        s += "0"

print(s)