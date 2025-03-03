import flet as ft
from objects import appWidth,appHeight,NavButton,ElevatedButton
from views.home import playlists
import os

def PlaylistsContent():
    playlistPath = "assets/playlistBank"
    information = [
        {
            "name": folder,
            "image": os.listdir(os.path.join(playlistPath,folder,"metadata"))[0],
            "songs": [
                song for song in os.listdir(os.path.join(playlistPath, folder))
                if song.endswith(".mp3")
            ]
        } 
        for folder in os.listdir(playlistPath) 
        if os.path.isdir(os.path.join(playlistPath, folder))
    ]

    playlistContainer = ft.Container(width=appWidth,height=appHeight-190)

    # playlistContainer = ft.Container(width=appWidth,height=appHeight-190,
    #     content=ft.Row(
    #         controls=[
    #             ft.Container(
    #                 content=ft.Row(
    #                     controls=[
    #                         ft.Container(
    #                             width=appWidth/3.5,height=appWidth/3.5+30,bgcolor="#2d2e33",border_radius=ft.border_radius.vertical(top=5),
    #                             content=ft.Column(
    #                                 controls=[
    #                                     ft.Text(i["name"],size=14,width=appWidth/3.5,text_align=ft.TextAlign.CENTER),
    #                                     ft.Image(src=i["src"],width=appWidth/3.5,height=appWidth/3.5),
    #                                 ],
    #                                 spacing=4,
    #                                 alignment=ft.MainAxisAlignment.END
    #                             )
    #                         ),
    #                         ft.DataTable(height=appWidth/3.5+30,
    #                             columns=[
    #                                 ft.DataColumn(ft.Text("Song Name")),
    #                                 ft.DataColumn(ft.Text("Action"))
    #                             ],
    #                             rows=[
    #                                 ft.DataRow(
    #                                     cells=[
    #                                         ft.DataCell(ft.Text("yes")),
    #                                         ft.DataCell(ElevatedButton("Remove",100,None))
    #                                     ]
    #                                 )
    #                             ]
    #                         )
    #                     ]
    #                 ),
    #             ) for i in playlists
    #         ],
    #         wrap=True,
    #         spacing=24,
    #         run_spacing=24
    #     ),
    #     alignment=ft.alignment.top_left
    # )
    content = ft.Container(width=appWidth,height=appHeight,
        content = ft.Column(
            controls=[
                ft.Text("View Playlists",size=30,weight="bold"),
                ft.Divider(thickness=2,height=4),
                # playlistContainer,
                # ElevatedButton("Upload Playlist",150,None),
                ft.Divider(thickness=2,height=4),
                NavButton("Return Home",lambda _:_.page.go("/home"),appWidth)
            ]
        )        
    )
    return content