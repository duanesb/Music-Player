import flet as ft
from objects import appWidth,appHeight,baseColor
import ffmpeg


def HomeContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Music Player",size=30,weight="bold")
            ]
        )
    )
    return content