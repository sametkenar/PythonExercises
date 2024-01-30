def find_median(grades):
    sorted_grades = sorted(grades)
    length = len(sorted_grades)
    middle_index = length // 2

    if length % 2 == 0 :
        median = (sorted_grades[middle_index -1] + sorted_grades[middle_index]) // 2
    else:
        median = sorted_grades[middle_index]
    
    return median

my_grades = [27,48,9,63,99,61,33,80,43,84,39,46,40,46,16,55,69,43,11,57]
median_grade = find_median(my_grades)
print("Median grade: ", median_grade)

    