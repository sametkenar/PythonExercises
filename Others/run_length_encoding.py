# Run-length Encoding

text = "aaaaaaxxxxmyyyaaaassssssssstttuivvvv"
code_list = []
last_character = text[0]
count = 1

# Go over each character except for the first
for curr_character in text[1:]:
    # If curr_character is equal to last_character, we found a duplicate
    if last_character == curr_character:
        count += 1
    else:
        # We have finished a sequence of same characters: Save the count and
        # reinitiliaze last_character and count accordingly
        code_list += [last_character if count==1 else [last_character, count]]
        count = 1
        last_character = curr_character

# handle the last_character here:
code_list += [last_character if count ==1 else [last_character, count]]

print(code_list)