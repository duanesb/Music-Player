import flet as ft
import os
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# import threading
# import time
# from pygame import mixer #! Not necessary anymore
from objects import appWidth, appHeight, NavButton, ElevatedButton, ActionButton
# mixer.init()
globalAudio = fta.Audio(src="playlistBank/TestPlay/All at Once.mp3", autoplay=False) #! Create a global audio object to replace the mixer
=======
import threading
import time
=======
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
=======
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
=======
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
from pygame import mixer
from objects import appWidth, appHeight, NavButton, ElevatedButton, ActionButton

mixer.init()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 48fed34 (Fixes)
current_index = 0
def PlaySong(song_list):
    global current_index
    # Reset to the beginning if we've reached the end
    if current_index >= len(song_list):
        current_index = 0
    song_path = song_list[current_index]
<<<<<<< HEAD
    print(song_path)
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
    globalAudio.src = song_path #! Changing song path based on your algorightm
    globalAudio.update()
    globalAudio.play() #! Play the song, duh
    # mixer.music.load(song_path)
    # mixer.music.set_volume(1)
    # mixer.music.play()
    # threading.Thread(target=monitor_song, daemon=True).start()

def PauseSong():
    # mixer.music.pause()
    globalAudio.pause() #! Mixer replacement

def UnpauseSong():
    # mixer.music.unpause()
    globalAudio.resume() #! Mixer replacement

def StopSong():
    # mixer.music.stop()
    globalAudio.seek(0)
    globalAudio.pause() #! Mixer replacement
=======
=======

# Function to play a song
def PlaySong(song_list, index=0):
    if index < len(song_list):
        song_path = song_list[index]

        def play_next():
            mixer.music.stop()
            PlaySong(song_list, index + 1)  # Move to the next song
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))

        mixer.music.load(song_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        mixer.music.set_endevent(ft.FLET_EVENT)

        ft.app.subscribe_event(ft.FLET_EVENT, lambda _: play_next())

=======

# Function to play a song
def PlaySong(song_list, index=0):
    if index < len(song_list):
        song_path = song_list[index]

        def play_next():
            mixer.music.stop()
            PlaySong(song_list, index + 1)  # Move to the next song

        mixer.music.load(song_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        mixer.music.set_endevent(ft.FLET_EVENT)

        ft.app.subscribe_event(ft.FLET_EVENT, lambda _: play_next())

>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
=======

# Function to play a song
def PlaySong(song_list, index=0):
    if index < len(song_list):
        song_path = song_list[index]

        def play_next():
            mixer.music.stop()
            PlaySong(song_list, index + 1)  # Move to the next song

        mixer.music.load(song_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        mixer.music.set_endevent(ft.FLET_EVENT)

        ft.app.subscribe_event(ft.FLET_EVENT, lambda _: play_next())

>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
# Function to Pause
def PauseSong():
    mixer.music.pause()

# Function to Unpause
def UnpauseSong():
    mixer.music.unpause()

# Function to Stop
def StopSong():
    mixer.music.stop()
>>>>>>> parent of 48fed34 (Fixes)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def SkipSong(song_list):
    global current_index
    # Increment the index, and loop back if needed
    current_index += 1
    if current_index >= len(song_list):
        current_index = 0  # Loop back to the first song
<<<<<<< HEAD
    # mixer.music.stop()
    globalAudio.seek(0)
    globalAudio.pause() #! Mixer replacement

    PlaySong(song_list)
    print("Current index:", current_index)
=======
=======
# Function to Skip to the next song
def SkipSong(song_list, current_index):
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
=======
# Function to Skip to the next song
def SkipSong(song_list, current_index):
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
=======
# Function to Skip to the next song
def SkipSong(song_list, current_index):
>>>>>>> parent of 62ae30c (FINALLY BRO (fixed skipping))
    mixer.music.stop()
    PlaySong(song_list, current_index + 1)  # Move to the next song

>>>>>>> parent of 48fed34 (Fixes)
def PlaylistsContent():
    playlistPath = "assets/playlistBank"
    information = [
        {
            "name": folder,
            "img": os.path.abspath(os.path.join(playlistPath, folder, "metadata", os.listdir(os.path.join(playlistPath, folder, "metadata"))[0])),
            "songs": [
                os.path.join(playlistPath, folder, song) for song in os.listdir(os.path.join(playlistPath, folder))
                if song.endswith(".mp3")
            ]
        } 
        for folder in os.listdir(playlistPath) 
        if os.path.isdir(os.path.join(playlistPath, folder))
    ]
<<<<<<< HEAD
=======

>>>>>>> parent of 48fed34 (Fixes)
    playlistContainer = ft.Column(
        width=appWidth, height=appHeight-190,
        controls=[
            ft.Container(  # PLAYLIST
                content=ft.Row(
                    controls=[
                        ft.Container(  # PLAYLIST NAME AND IMAGE
                            width=appWidth / 3.5, height=appWidth / 3.5 + 30, bgcolor="#2d2e33",
                            border_radius=ft.border_radius.vertical(top=5),
                            content=ft.Column(
                                controls=[
                                    ft.Text(playlist["name"], size=14, width=appWidth / 3.5, text_align=ft.TextAlign.CENTER),
                                    ft.Image(playlist["img"], width=appWidth / 3.5, height=appWidth / 3.5)
                                ],
                                spacing=4,
                                alignment=ft.MainAxisAlignment.END
                            )
                        ),
                        ft.DataTable(  # SONG LIST
                            columns=[
                                ft.DataColumn(ft.Text("Song Name")),
                                ft.DataColumn(ft.Text("Action"))
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(os.path.basename(song)[:-4], size=10)),
                                        ft.DataCell(ft.ElevatedButton("Remove", height=20))
                                    ]
                                ) for song in playlist["songs"]
                            ],
                            column_spacing=0, width=200
                        ),
                        ft.Column(  # PLAY, PAUSE, UNPAUSE, STOP, AND SKIP BUTTONS
                            controls=[
                                ElevatedButton("Play", 100, lambda _, songs=playlist["songs"]: PlaySong(songs)),
                                ElevatedButton("Pause", 100, lambda _: PauseSong()),
                                ElevatedButton("Unpause", 100, lambda _: UnpauseSong()),
                                ElevatedButton("Stop", 100, lambda _: StopSong()),
                                ElevatedButton("Skip", 100, lambda _, songs=playlist["songs"]: SkipSong(songs, 0))

        
                            ]
                        )
                    ]
                )
            ) for playlist in information
        ],
        scroll=True
    )
<<<<<<< HEAD
=======

>>>>>>> parent of 48fed34 (Fixes)
    content = ft.Container(
        width=appWidth, height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("View Playlists", size=30, weight="bold"),
                ft.Divider(thickness=2, height=4),
                playlistContainer,
                ft.Divider(thickness=2, height=4),
<<<<<<< HEAD
                NavButton("Return Home", lambda _: _.page.go("/home"), appWidth),
            ]
        ),
=======
                NavButton("Return Home", lambda _: _.page.go("/home"), appWidth)
            ]
        )
>>>>>>> parent of 48fed34 (Fixes)
    )
    return content
