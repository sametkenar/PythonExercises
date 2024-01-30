def maximum_occurence(numbers):
    # Create a dictionary to count occurences of each number
    occurrence_count = {}

    # Count occurences of each number in the list
    for number in numbers:
        if number in occurrence_count:
            occurrence_count[number] += 1
        else:
            occurrence_count[number] = 1

    # Find the number with the maximum occurence
    max_occurrence = max(occurrence_count, key=occurrence_count.get)

    return max_occurrence

# Example Usage
number_list = [1, 3, 5, 3, 2, 5, 1, 7, 7, 7]
result = maximum_occurence(number_list)
print("Number with maximum occurence: ", result) # Output: 7 


