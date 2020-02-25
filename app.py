
import os
import random
from pygame import mixer

music_dirs = []

# source = /home/ali/Music

print("My Music Folder : /home/ali/Music ")
print("BTW You Can Enter '/' Too Scan All Your Directories (Not Recomended)")
print("We Only Scan 'MP3', 'AVI', 'FLAC', 'M4A'")

source = input("Pls Enter The Music Folder: ")

for (root, dirs, files) in os.walk(source, topdown=True):
    if files:
        for i in range(len(files)):
            if files[i].lower().endswith(('.mp3', '.avpipi', '.flac', 'm4a')):
                dir = root + "/" + files[i]
                music_dirs.append(dir)


mixer.init()
index = 0
curr_song = ''

def nextsong(index):
    mixer.music.load(music_dirs[index])
    print(music_dirs[index])
    curr_song = music_dirs[index]
    mixer.music.play()


def play_a_different_song(curr_song, index):
    print(index)
    index = random.choice(range(len(music_dirs)))
    print(index)
    next_song = music_dirs[index]
    while next_song == curr_song:
        index = random.choice(range(len(music_dirs)))
        next_song = music_dirs[index]
        print(next_song)
    mixer.music.load(next_song)
    print(next_song)
    mixer.music.play()
    return index

print(music_dirs[0])
mixer.music.load(music_dirs[0])
mixer.music.play()

print(music_dirs[22])
while True:
    print("Enter p ---> pause")
    print("Enter r ---> resume")
    print("Enter n ---> next")
    print("Enter m ---> suffle next")
    print("Enter q ---> exit")

    query = input("Commad: ")
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'n':
        index += 1
        mixer.music.fadeout(1)
        nextsong(index)
    elif query == 'm':
        mixer.music.fadeout(1)
        index = play_a_different_song(curr_song, index)
    elif query == 'q':
        mixer.music.stop()
        break