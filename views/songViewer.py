import flet as ft
from objects import appWidth,appHeight,NavButton

def SongViewerContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Song Viewer",size=30,weight="bold"),
                ft.Divider(thickness=2,height=4),
                NavButton("Return Home",lambda _:_.page.go("/home"),appWidth)
            ]
        )
    )

    return content