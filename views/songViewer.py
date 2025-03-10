import flet as ft
from objects import appWidth,appHeight,NavButton
from mutagen.mp3 import MP3 as mp3
import os

def SongViewerContent():
    songContainer = ft.Container(width=appWidth,height=appHeight-190,
        content=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Song Name")),
                ft.DataColumn(ft.Text("Artist")),
                ft.DataColumn(ft.Text("Duration")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(i[:-4].split('-')[1])),
                        ft.DataCell(ft.Text(i[:-4].split('-')[0])),
                        ft.DataCell(ft.Text(f"{int(mp3(f"assets/songBank/{i}").info.length)//60}:{(int(mp3(f"assets/songBank/{i}").info.length)%60):02d}"))
                    ]
                ) for i in os.listdir("assets/songBank")
            ]
        )
    )
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Song Viewer",size=30,weight="bold"),
                ft.Divider(thickness=2,height=4),
                songContainer,
                ft.Divider(thickness=2,height=4),
                NavButton("Return Home",lambda _:_.page.go("/home"),appWidth)
            ]
        )
    )

    return content