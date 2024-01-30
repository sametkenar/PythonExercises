def grade_student(answer_key_file, student_answers_file):
    # Read the answer key from the answer key file
    answer_key = {}
    with open(answer_key_file, "r") as key_file:
        for line in key_file:
            parts = line.strip().split()
            question_number = int(parts[0])
            correct_answer = parts[1]
            grade = int(parts[2])
            answer_key[question_number] = (correct_answer, grade)

    total_grade = 0

    # Read the student's answers and calculate the total grade
    with open(student_answers_file, "r") as student_file:
        for line in student_file:
            parts = line.strip().split()
            question_number = int(parts[0])
            student_answer = parts[1]
            if question_number in answer_key:
                correct_answer, grade = answer_key[question_number]
                if student_answer == correct_answer:
                    total_grade += grade

    return total_grade

print(grade_student("answer_key.txt", "student.txt"))
    