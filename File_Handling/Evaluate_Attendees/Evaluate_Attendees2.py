def evaluate_attendees(answer_key_file, responses_file):
    # Read the answer key from the answer key file
    with open(answer_key_file, 'r') as key_file:
        answer_key = key_file.readline().strip().split()

    attendee_points = []

    # Read the responses file and calculate points for each attendee
    with open(responses_file, 'r') as responses:
        for line in responses:
            parts = line.strip().split()
            name = parts[0]
            responses = parts[1:]

            correct_answers = sum(1 for a, b in zip(answer_key, responses) if a == b)
            wrong_answers = len(answer_key) - correct_answers
            point = correct_answers - wrong_answers * 0.25

            attendee_points.append((name, point))

    # Sort the attendee points in descending order of points
    sorted_attendee_points = sorted(attendee_points, key=lambda x: x[1], reverse=True)

    return sorted_attendee_points

# Example usage
answer_key_file = "key.txt"
responses_file = "attendees.txt"
result = evaluate_attendees(answer_key_file, responses_file)
for name, point in result:
    print(f"{name}: {point}")
