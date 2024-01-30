def reverse_left(i_list, occurrence):
    occurrence_index = i_list.index(occurrence)         #finding the index of the first occurrence

    left_sub_list = i_list[:occurrence_index]            #constructing the left sub-list
    left_sub_list.reverse()                             #reversing the left sub-list
    right_sub_list = i_list[occurrence_index:]          #constructing the right sub-list

    return left_sub_list + right_sub_list

print(reverse_left([8,1,4,5,6,6,3,2],6))
print(reverse_left([64, 51, 77, 34, 77, 39, 57, 67, 58, 63, 51],39))

