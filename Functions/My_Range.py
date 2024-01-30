def my_range(start, stop, step):
    if(stop < start):
        return []
    else:
        return [start] + my_range(start + step, stop, step) # note that left side is always
        # always a list and right side will be list even it is empty.


print(my_range(3, 10, 1))
print(my_range(3, 9, 2))
