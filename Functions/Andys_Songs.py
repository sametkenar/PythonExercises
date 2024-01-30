def andys_songs(song_list, mood):
    can_play = 0
    for song in song_list:
        if song <= mood:
            can_play +=1
    return can_play 


print(andys_songs([2,7,12,5,1,0,6,8],5))
print(andys_songs([4,8,15,16,23,42,108,271,49,88],55))