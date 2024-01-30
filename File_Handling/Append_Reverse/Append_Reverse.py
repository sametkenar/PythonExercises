def append_reverse(input_file_name):
    person_list = []
    input_file = open(input_file_name, "r")
    for line in input_file:
        name, surname = line.split()
        # Save as a tuple
        person_list.append((name,surname))


    input_file.close()
    # Re-open in append mode
    input_file = open(input_file_name, "a")
    for person in person_list:
        # first is name, second is surname
        string_to_write = person[1] + " " + person[0] + "\n"
        input_file.write(string_to_write)

    
    input_file.close()
    return person_list

print(append_reverse("input.txt"))