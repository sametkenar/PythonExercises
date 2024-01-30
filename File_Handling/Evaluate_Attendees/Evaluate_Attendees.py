def evaluate_attendees(key_path, grade_path):
    attendees = []

    key_file = open(key_path, "r")
    key = key_file.read().split()
    key_file.close()

    questions = len(key)

    input_file = open(grade_path, "r")
    for line in input_file.readlines():
        correct = 0
        wrong = 0
        name = line.split()[0]          # seperating name from the rest of the list
        responses = line.split()[1:]    # getting the responses for the exam
        for i in range(questions):      # checking responses one by one to determine result
            if responses[i] == key[i]:
                correct += 1
            else:
                wrong += 1
        attendees.append((name, correct - 0.25 * wrong))

    input_file.close() 

    attendees_sorted = sorted(attendees, key=lambda item: item[1], reverse = True)  # sort the list according to points  
    return attendees_sorted

print(evaluate_attendees("key.txt", "attendees.txt"))