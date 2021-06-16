"""
A Python script to create attributes of a song.
Then printing those variable on the console.
"""
import function as func

# Title of the song
Title = "Numb"

# Artist of the song
Artist = "Linkin Park"

# Album of the song
Album = func.albumName()

# Year of release of this song
Year = func.albumYear()

# Duration of the song
Duration = func.getDuration(True)

# Genre of the song
Genre = "Alternative rock, Nu metal, Alt Metal"

# lyrics for the song
Lyrics = func.getLyrics()

# Displaying attributes of the song
print("Title :", Title)
print("Artist :", Artist)
print("Album :", Album)
print("Genre :", Genre)
print("Year of Release :", Year)
print("Duration :", Duration)
print("Lyrics :", Lyrics)
