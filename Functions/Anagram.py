def anagram(str1, str2):
    count_1 = {}
    for char in str1:
        if char in count_1:
            count_1[char] +=1
        else:
            count_1[char] = 1

    count_2 = {}
    for char in str2:
        if char in count_2:
            count_2[char] += 1
        else:
            count_2[char] = 1

    if count_1 == count_2:
        return True
    else:
        return False


print(anagram("palm","lamp"))
print(anagram("hello","olla"))