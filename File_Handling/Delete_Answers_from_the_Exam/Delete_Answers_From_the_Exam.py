def delete_answers(input_path):
    count = 1
    lines = []

    input_file = open(input_path, "r")
    lines = input_file.readlines()
    input_file.close()

    output_file = open("new_questions.txt", "w")
    for line in lines:
        if (count%6 == 0):
            count += 1
            continue
        else:
            output_file.write(line)
            count += 1
    
    output_file.close()

print(delete_answers("questions.txt"))    