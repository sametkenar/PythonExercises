human = input()
human_says = list(human)

n = len(human_says)
right_count = 0

for i in range(0,n):
    if i%2 == 0:
        if human_says[i] == 'u':
            right_count = right_count + 1
    else:
        if human_says[i] == 'h':
            right_count = right_count + 1

if right_count == n:
    print("Are you sad, hooman?")
else:
    print("I am so sad, hooman.")