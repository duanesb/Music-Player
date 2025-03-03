import flet as ft
import os
from pygame import mixer
from objects import appWidth, appHeight, NavButton, ElevatedButton

mixer.init()

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

# Function to Pause
def PauseSong():
    mixer.music.pause()

# Function to Unpause
def UnpauseSong():
    mixer.music.unpause()

# Function to Stop
def StopSong():
    mixer.music.stop()

# Function to Skip to the next song
def SkipSong(song_list, current_index):
    mixer.music.stop()
    PlaySong(song_list, current_index + 1)  # Move to the next song

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

    content = ft.Container(
        width=appWidth, height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("View Playlists", size=30, weight="bold"),
                ft.Divider(thickness=2, height=4),
                playlistContainer,
                ft.Divider(thickness=2, height=4),
                NavButton("Return Home", lambda _: _.page.go("/home"), appWidth)
            ]
        )
    )
    return content
