def average_weight(input_path):
    min_weight = 45
    max_weight = 125
    weights_in_range = []
    input_file = open(input_path, 'r')  # open input file in read mode
    for line in input_file.readlines():
        all_weights = list(map(int,list(line.split()))) # getting integer values in a line.
        filtered = list(filter(lambda x: int(x) >= min_weight and int(x) <= max_weight, all_weights)) # filtering the weights
        weights_in_range += filtered

    input_file.close()      # do not forget to close

    count = 0
    total = 0
    for w in weights_in_range:
        total += w
        count += 1
    if count:
        return (total/count)
    else: 
        return 0 
    
print(average_weight("input.txt"))