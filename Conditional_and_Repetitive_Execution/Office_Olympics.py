def pick_winners(lst):
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return [x[0] for x in lst[:3]]

x = eval(input())

print(pick_winners(x))



