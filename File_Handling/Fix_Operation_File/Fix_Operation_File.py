def fix_operation_file(input_file_name, output_file_name):
    operation_results = []

    # Open files in read and write modes, respectively
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")
    count = 0
    operation_string = ""

    # Read lines from input file
    for line in input_file:
        # Add the number or operator to operation string to save
        # Get rid of the new line character
        operation_string += line.rstrip("\n")

        count += 1

        # If an operation is read completely
        if count == 3:
            output_file.write(operation_string)
            output_file.write("\n")

            # Use eval to evaluate the operation in operation string
            operation_results.append(eval(operation_string))

            # Reset the count and operation string
            count = 0
            operation_string = ""

        # closing the files
    input_file.close()
    output_file.close()
    return operation_results

print(fix_operation_file("input.txt","output.txt"))
    

