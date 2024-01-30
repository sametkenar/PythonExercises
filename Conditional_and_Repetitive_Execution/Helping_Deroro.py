W = int(input())
A = int(input())
B = int(input())

result = False

for i in range(0, W+1, A):    # notice the 3rd argument as step-size in the range function
    for j in range(0, W+1, B):
        if(i + j == W):
            result = True

if result == True:
    print("YES")
else:
    print("NO")