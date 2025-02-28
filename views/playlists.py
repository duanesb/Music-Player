import flet as ft
from objects import appWidth,appHeight

def PlaylistsContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content = ft.Column(
            controls=[
                ft.Text("yay")
            ]
        )        
    )
    return content