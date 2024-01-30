def dice_game(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    player_names = lines[0].strip().split()
    dice_numbers = [list(map(int, line.strip().split())) for line in lines[1:]]

    points = [0] * len(player_names)

    for round_dice in dice_numbers:
        max_dice = max(round_dice)
        num_of_max_dice = round_dice.count(max_dice)

        if num_of_max_dice == 1:
            max_player_index = round_dice.index(max_dice)
            points[max_player_index] += 1
        else:
            for i in range(len(player_names)):
                if round_dice[i] == max_dice:
                    points[i] += 1 / num_of_max_dice
        
        max_points = max(points)
        winners = [player_names[i] for i,p in enumerate(points) if p == max_points]

        if len(winners) == 1:
            winner_info = f"Winner: {winners[0]}, Points: {max_points:.2f}"
        else:
            winner_info = f"Draw: {','.join(winners)}, Points each: {max_points / len(winners):.2f}"

        return winner_info

# Example Usage
input_file = "input.txt"
input_file1 = "input1.txt"
result = dice_game(input_file)
result1 = dice_game(input_file1)
print(result)
print(result1)