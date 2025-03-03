import flet as ft
from objects import appWidth,appHeight,NavButton,ElevatedButton
from views.home import playlists
import os

def PlaylistsContent():
    playlistPath = "assets/playlistBank"
    information = [
        {
            "name": folder,
            "img": os.listdir(os.path.join(playlistPath,folder,"metadata"))[0],
            "songs": [
                song for song in os.listdir(os.path.join(playlistPath, folder))
                if song.endswith(".mp3")
            ]
        } 
        for folder in os.listdir(playlistPath) 
        if os.path.isdir(os.path.join(playlistPath, folder))
    ]

    playlistContainer = ft.Column(width=appWidth,height=appHeight-190,
        controls=[
            ft.Container( # PLAYLIST
                content = ft.Row(
                    controls= [
                        ft.Container( # PLAYLIST NAME AND IMAGE
                            width=appWidth/3.5, height=appWidth/3.5+30,bgcolor="#2d2e33",
                            border_radius=ft.border_radius.vertical(top=5),
                            content=ft.Column(
                                controls=[
                                    ft.Text(playlist["name"],size=14,width=appWidth/3.5,text_align=ft.TextAlign.CENTER),
                                    ft.Image(playlist["img"],width=appWidth/3.5,height=appWidth/3.5)
                                ],
                                spacing=4,
                                alignment=ft.MainAxisAlignment.END
                            )
                        ),
                        ft.DataTable( # SONG AND ACTIONS
                            columns=[
                                ft.DataColumn(ft.Text("Song Name")),
                                ft.DataColumn(ft.Text("Action"))
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(song[:-4],size=10)),
                                        ft.DataCell(ft.ElevatedButton("Remove",height=15))
                                    ]
                                )  for song in playlist["songs"]
                            ],
                            column_spacing=0
                        )
                    ]
                )
            ) for playlist in information
        ],
        scroll=True
    )
    content = ft.Container(width=appWidth,height=appHeight,
        content = ft.Column(
            controls=[
                ft.Text("View Playlists",size=30,weight="bold"),
                ft.Divider(thickness=2,height=4),
                playlistContainer,
                ft.Divider(thickness=2,height=4),
                NavButton("Return Home",lambda _:_.page.go("/home"),appWidth)
            ]
        )        
    )
    return content