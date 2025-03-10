import flet as ft
import flet_audio as fta #! You need to install the official audio handling module for this, the default one will be deprecated in the future
import os
import threading
import time
from pygame import mixer
# import threading
# import time
# from pygame import mixer #! Not necessary anymore
from objects import appWidth, appHeight, NavButton, ElevatedButton, ActionButton

mixer.init()
# mixer.init()
globalAudio = fta.Audio(src="playlistBank/TestPlay/All at Once.mp3", autoplay=False) #! Create a global audio object to replace the mixer
current_index = 0

def PlaySong(song_list):
@@ -15,40 +17,52 @@ def PlaySong(song_list):
        current_index = 0

    song_path = song_list[current_index]
    print(song_path)

    def monitor_song():
        global current_index
        # Wait until the current song finishes
        while mixer.music.get_busy():
            time.sleep(0.5)
        # Increment and reset the index if necessary
        current_index += 1
        if current_index >= len(song_list):
            current_index = 0  # Loop back to first song
        PlaySong(song_list)
    # def monitor_song():
    #     global current_index
    #     # Wait until the current song finishes
    #     while globalAudio.get_current_position() < globalAudio.get_duration():
    #         time.sleep(0.5)
    #     # Increment and reset the index if necessary
    #     current_index += 1
    #     if current_index >= len(song_list):
    #         current_index = 0  # Loop back to first song
    #     PlaySong(song_list)

    mixer.music.load(song_path)
    mixer.music.set_volume(1)
    mixer.music.play()
    globalAudio.src = song_path #! Changing song path based on your algorightm
    globalAudio.update()
    globalAudio.play() #! Play the song, duh

    threading.Thread(target=monitor_song, daemon=True).start()
    # mixer.music.load(song_path)
    # mixer.music.set_volume(1)
    # mixer.music.play()

    # threading.Thread(target=monitor_song, daemon=True).start()

def PauseSong():
    mixer.music.pause()
    # mixer.music.pause()
    globalAudio.pause() 

def UnpauseSong():
    mixer.music.unpause()
    # mixer.music.unpause()
    globalAudio.resume()

def StopSong():
    mixer.music.stop()
    # mixer.music.stop()
    globalAudio.seek(0)
    globalAudio.pause()

def SkipSong(song_list):
    global current_index
    # Increment the index, and loop back if needed
    current_index += 1
    if current_index >= len(song_list):
        current_index = 0  # Loop back to the first song
    mixer.music.stop()
    # mixer.music.stop()
    globalAudio.seek(0)
    globalAudio.pause()

    PlaySong(song_list)
    print("Current index:", current_index)

@@ -130,8 +144,8 @@ def PlaylistsContent():
                ft.Divider(thickness=2, height=4),
                playlistContainer,
                ft.Divider(thickness=2, height=4),
                NavButton("Return Home", lambda _: _.page.go("/home"), appWidth)
                NavButton("Return Home", lambda _: _.page.go("/home"), appWidth),
            ]
        )
        ),
    )
    return content