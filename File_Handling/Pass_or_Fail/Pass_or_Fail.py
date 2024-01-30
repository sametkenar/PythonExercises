def pass_or_fail(input_file, output_file):
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    results = []

    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]
        first_midterm = int(parts[1])
        second_midterm = int(parts[2])
        final_exam = int(parts[3])

        overall_grade = 0.3 * first_midterm + 0.3 * second_midterm + 0.4 * final_exam

        status = "Pass" if overall_grade >= 60 else "Fail"
        results.append(f"{name},{status}\n")

    with open(output_file, "w") as output_f:
        output_f.writelines(results)

# Example usage
input_file = "input.txt"
output_file = "output.txt"
input_file1 = "input1.txt"
output_file1 = "output1.txt"

print(pass_or_fail(input_file,output_file))
print(pass_or_fail(input_file1,output_file1))
