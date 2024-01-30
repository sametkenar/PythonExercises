# This solution uses is an optimization technique called
# memorization.

W = int(input())
A = int(input())
B = int(input())

achievable = {0: True}

for i in range(0, W):
    if(i in achievable):
        achievable[i+A] = True
        achievable[i+B] = True

if W in achievable:
    print("YES")
else:
    print("NO")