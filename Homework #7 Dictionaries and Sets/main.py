favSong = {"Title" : "Numb","Artist" : "Linkin Park","Album" : "Meteora","Year" : 2003,"Duration" : "03:05","Genre" : ["Alternative rock", "Nu metal", "Alt Metal"]}

def guessTheValue(key,guessvalue):
    if favSong[key].lower() == guessvalue.lower():
        return True
    return False

def askForInput(key,message):
    return guessTheValue(key,input(message))

if askForInput("Title","Can you guess my favourite song's name?\n"):
    print("Congratulations you have guessed the song correctly")
else:
    print("Sorry your guess is wrong.\nMy favourite song is",favSong["Title"])

if askForInput("Artist","Can you guess the song's artist?\n"):
    print("Congratulations you have guessed the artist correctly")
else:
    print("Sorry your guess is wrong.\nArtist of the song is",favSong["Artist"])

print("\nDetails for the Song")
for key in favSong:
    print(key ," : ",favSong[key])