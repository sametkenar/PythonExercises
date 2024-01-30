s = input()

cursor = ""         # to keep the current character
streak = 1
buildup = ""

for a in s:
    if a != cursor:
        if cursor != "":
            buildup += str(streak) + cursor     # notice the casting in to string
        cursor = a
        streak = 1
    else:
        streak += 1
buildup += str(streak) + cursor

print(buildup)

