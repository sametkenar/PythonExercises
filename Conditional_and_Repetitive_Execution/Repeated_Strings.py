string = input()
result = "Yes"
if len(string) % 2 == 0:
    for index in range(0, int(len(string)/2)):
        if string[index] != string[int(len(string)/2) + index]:
            result = "No"
            break
else:
    result = "Error"

print(result)