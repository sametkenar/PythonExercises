def cheapest_flour(input_path, output_path):

    prices_per_kg = []

    with open(input_path, "r") as input_file:    # opening the file in read mode
       for line in input_file.readlines():
           brand = list(map(int,list(line.split()))) # getting integer values in a line.
           price = brand[0]
           weight = brand[1]
           prices_per_kg.append(price/weight)

    prices_per_kg.sort(reverse=True)             # sorting in decreasing order

    with open(output_path, "w") as output_file:     # opening the file in write mode
        for brand in prices_per_kg:
            output_file.write(str(brand)+ "\n") # print values into the file with newlines



print(cheapest_flour("input.txt", "output.txt"))