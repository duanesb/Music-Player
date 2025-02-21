import flet as ft

global appWidth, appHeight, baseColor
appWidth = 500
appHeight = 500
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
            bgcolor="#808080",
            shape=ft.RoundedRectangleBorder(radius=5),
            side=ft.BorderSide(width=3,color="#575757")
        )
        self.on_click = function

class TextField(ft.TextField):
    def __init__(self,text,function):
        super().__init__()
        self.height=40
        self.width=100
        self.text=text
        self.color="black"
        self.style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=15,weight="bold"),
            bgcolor="#808080",
            shape=ft.RoundedRectangleBorder(radius=5),
            side=ft.BorderSide(width=3,color="#575757")
        )
        self.on_click = function