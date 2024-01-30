def ball_game(list_of_children, number_of_turns):
    t = 0
    i = 0
    while t < number_of_turns:
        try:
            i = list_of_children[i]
        except IndexError:
            break
        t += 1
    return i 

print(ball_game([1, 3, 2], 1))
print(ball_game([1, 3, 2], 2))
print(ball_game([1, 3, 2], 3))
print(ball_game([3,4,5,1,2], 4))
print(ball_game([3,4,5,1,2], 5))
print(ball_game([3,4,5,1,2], 6))
print(ball_game([8,7,1,5,3,10,4,2,6,9],4))
print(ball_game([8,7,1,5,3,10,4,2,6,9],5))
print(ball_game([8,7,1,5,3,10,4,2,6,9],6))
print(ball_game([8,7,1,5,3,10,4,2,6,9],7))