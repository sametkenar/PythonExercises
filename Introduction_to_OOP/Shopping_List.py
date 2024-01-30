def readable(s):
    l = s.split(",")
    for i in l:
        print(i.strip().lower())

print(readable("LemOn, gaRlic, PAsta"))
print(readable("CheeSe, cHeeSe, CHEESE"))