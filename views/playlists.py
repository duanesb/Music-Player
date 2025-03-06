import flet as ft
import flet_audio as fta #! You need to install the official audio handling module for this, the default one will be deprecated in the future
import os
# import threading
# import time
# from pygame import mixer #! Not necessary anymore
from objects import appWidth, appHeight, NavButton, ElevatedButton, ActionButton

# mixer.init()
globalAudio = fta.Audio(src="playlistBank/TestPlay/All at Once.mp3", autoplay=False) #! Create a global audio object to replace the mixer
current_index = 0

def PlaySong(song_list):
    global current_index
    # Reset to the beginning if we've reached the end
    if current_index >= len(song_list):
        current_index = 0

    song_path = song_list[current_index]
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

def SkipSong(song_list):
    global current_index
    # Increment the index, and loop back if needed
    current_index += 1
    if current_index >= len(song_list):
        current_index = 0  # Loop back to the first song
    # mixer.music.stop()
    globalAudio.seek(0)
    globalAudio.pause() #! Mixer replacement
    
    PlaySong(song_list)
    print("Current index:", current_index)

def PlaylistsContent():
    playlistPath = "assets/playlistBank"
    information = [
        {
            "name": folder,
            "img": os.path.abspath(os.path.join(playlistPath, folder, "metadata",
                                                   os.listdir(os.path.join(playlistPath, folder, "metadata"))[0]))
                   if os.listdir(os.path.join(playlistPath, folder, "metadata")) else "",
            "songs": [
                os.path.join(playlistPath, folder, song)
                for song in os.listdir(os.path.join(playlistPath, folder))
                if song.endswith(".mp3")
            ]
        }
        for folder in os.listdir(playlistPath)
        if os.path.isdir(os.path.join(playlistPath, folder))
    ]

    playlistContainer = ft.Column(
        width=appWidth, height=appHeight - 190,
        controls=[
            ft.Container(  # PLAYLIST
                content=ft.Row(
                    controls=[
                        ft.Container(  # PLAYLIST NAME AND IMAGE
                            width=appWidth / 3.5, height=appWidth / 3.5 + 30, bgcolor="#2d2e33",
                            border_radius=ft.border_radius.vertical(top=5),
                            content=ft.Column(
                                controls=[
                                    ft.Text(playlist["name"], size=14, width=appWidth / 3.5,
                                            text_align=ft.TextAlign.CENTER),
                                    ft.Image(playlist["img"], width=appWidth / 3.5,
                                             height=appWidth / 3.5) if playlist["img"] else None
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
                                ElevatedButton("Skip", 100, lambda _, songs=playlist["songs"]: SkipSong(songs))
                            ]
                        )
                    ]
                )
            )
            for playlist in information
        ],
        scroll=True
    )

    content = ft.Container(
        width=appWidth, height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("View Playlists", size=30, weight="bold"),
                ft.Divider(thickness=2, height=4),
                playlistContainer,
                ft.Divider(thickness=2, height=4),
                NavButton("Return Home", lambda _: _.page.go("/home"), appWidth),
            ]
        ),
    )
    return content
