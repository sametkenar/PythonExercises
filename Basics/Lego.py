lego = eval(input())
s = int(input())
e = int(input())

lego[s-1:e] = [0] * (e-s+1) # notice the slicing and repetition operators

print(lego)
