playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]


print("Alef - Tedad:")
print(len(playlist))
print("-------------------")


print("Be - Avalin va Akharin:")
print(playlist[0])   
print(playlist[-1])  

print("-------------------")


playlist.append("Dynamite")


playlist.remove("Believer")

playlist.sort()
print("Hey - List-e Mortab:")
print(playlist)
print("-------------------")

.
print("Vav - Chap ba Shomare:")
for index, song in enumerate(playlist, start=1):
    print(f"{index}. {song}")
