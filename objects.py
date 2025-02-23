import flet as ft

global appWidth, appHeight, baseColor
appWidth = 500
appHeight = 600
baseColor = "#1b1c1f"

class View(ft.View):
    def __init__(self,route,content):
        super().__init__(route=route)
        self.controls.append(content)
        self.bgcolor = baseColor

    def set(self,page):
        page.views.append(self)

class ElevatedButton(ft.ElevatedButton):
    def __init__(self,text,function):
        super().__init__()
        self.height=40
        self.width=100
        self.text=text
        self.color="black"
        self.style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=15,weight="bold"),
            bgcolor="#5f83b3",
            shape=ft.RoundedRectangleBorder(radius=4),
            side=ft.BorderSide(width=3,color="#446085")
        )
        self.on_click = function

class TextField(ft.TextField):
    def __init__(self,text,function):
        super().__init__()
        self.height=40
        self.width=appWidth-100
        self.hint_text=text
        self.hint_style= ft.TextStyle(color="black",size=15)
        self.color="black"
        self.bgcolor = "#c9c9c9"
        self.border_width = 3
        self.border_color = "#a1a1a1"
        self.on_click = function
        self.cursor_color = "black"

class NavButton(ft.ElevatedButton):
    def __init__(self,text,function,width):
        super().__init__()
        self.height=50
        self.width=width
        self.text=text
        self.color="black"
        self.style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=15,weight="bold"),
            bgcolor="#ffd154",
            shape=ft.RoundedRectangleBorder(radius=4),
            side=ft.BorderSide(width=3,color="#bd952a")
        )
        self.on_click = function

class playlistImage(ft.Container):
    def __init__(self):
        super().__init__(content=ft.Image("upload.png"))
        self.width=150
        self.height=150
        self.bgcolor="white"