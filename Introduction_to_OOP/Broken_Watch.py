def is_time_valid(s):
    l = s.split('.')
    if(len(l)!=2):
        return False
    if(l[0]<"00" or l[0]>"23"):
        return False
    if(l[1]<"00" or l[1]>"59"):
        return False
    return True

print(is_time_valid("23.20"))
print(is_time_valid("22.61"))
print(is_time_valid("ten past eleven"))


