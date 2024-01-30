lst = eval(input())

m = int(input())

n = len(lst)  # length of list

print(lst[(n-m) // 2 : (n+m) // 2])  # notice the slicing operator