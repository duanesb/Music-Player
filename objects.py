import flet as ft

global appWidth, appHeight, baseColor
appWidth = 500
appHeight = 600
baseColor = "white"

class View(ft.View):
    def __init__(self,route,content):
        super().__init__(route=route)
        self.controls.append(content)
        self.bgcolor = baseColor

    def set(self,page):
        page.views.append(self)

class ViewContainer(ft.Container):
    def __init__(self,content):
        super().__init__()
        self.width = appWidth
        self.height = appHeight
        self.content = content