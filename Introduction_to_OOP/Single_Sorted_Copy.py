def single_sorted_copy(lst):
    copied_lst = lst[:]         # slicing returns a shallow copy of the list
    for x in copied_lst:
        for i in range(copied_lst.count(x)-1):
            copied_lst.remove(x)
    copied_lst.sort()

    return copied_lst


print(single_sorted_copy([3,3,2,2,1,1]))
print(single_sorted_copy([1,3,2,2,1,1,4]))