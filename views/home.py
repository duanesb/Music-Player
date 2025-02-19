import flet as ft
from objects import appWidth,appHeight,baseColor

def HomeContent():
    content = ft.Container(width=appWidth,height=appHeight,bgcolor=baseColor,
        content=ft.Column(
            controls=[
                ft.Text("Home")
            ]
        )
    )
    return content