def format_for_migration(input_file, output_file):
    formatted_records = []

    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    for line in lines:
        actor,episode_count,last_occurence = line.strip().split(",")
        formatted_record = f"Actor:{actor},EpisodeCount:{episode_count},LastOccurence:{last_occurence}\n"
        formatted_records.append(formatted_record)

    with open(output_file, "w") as output_f:
        output_f.writelines(formatted_records)

    return len(formatted_records)

# Example Usage
input_file = "input.txt"
output_file = "output.txt"

formatted_count = format_for_migration(input_file,output_file)
print(f"Formatted {formatted_count} records.")