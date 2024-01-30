def increment_list(input_list):
    # Create a shallow copy of the input list using slicing
    new_list = input_list[:]

    # Increment all elements in the new list 
    for i in range(len(new_list)):
        new_list[i] += 1

    return new_list

# Example Usage

# original_list = [1, 2, 3, 4, 5]
# incremented_list = increment_list(original_list)

# print("Original list: ", original_list)         # Output: [1, 2, 3, 4, 5]
# print("Incremented list: ", incremented_list)   # Output: [2, 3, 4, 5, 6]

a = [1, 2, 3, 10, 15]
print(a)
print(increment_list(a))
print(a)