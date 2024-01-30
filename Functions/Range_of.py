# as the non-trivial solution

def range_of(lst):
    min_elem, max_elem = lst[0], lst[0]

    for elem in lst[1:]:
        if elem < min_elem:
            min_elem = elem
        elif elem > max_elem:
            max_elem = elem
    return max_elem - min_elem

print(range_of([1,4,6,28,-10,0,0,1]))
print(range_of([1]))
print(range_of([2,2]))
