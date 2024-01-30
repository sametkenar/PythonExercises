def substring_count(first, second):
    count = 0
    length_of_first = len(first)
    length_of_second = len(second)
    for i in range(0, length_of_first - length_of_second+1): # Notice the narrowing of the indices to possible occurrence range.
        if first[i:i+length_of_second] == second:
            count +=1
    return count

print(substring_count("stanrandysstancartmanstankenny", "stan"))
print(substring_count("taktakatutakatakataktuk", "ta"))
print(substring_count("ababa","aba"))