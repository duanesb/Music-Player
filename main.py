import flet as ft
from objects import appWidth,appHeight,baseColor,View
from views.home import HomeContent
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

def filePickerResult(e:ft.FilePickerResultEvent):
    if e.files:
        path = e.files[0].path

def main(page: ft.Page):
    # CONFIG
    page.title = "Music Player"
    page.window.width = appWidth
    page.window.height = appHeight

    # FILE PICKER
    filePicker = ft.FilePicker(on_result=filePickerResult)
    page.overlay.append(filePicker)

    # ROUTING
    def route_change(route):
        page.views.clear()
        match(page.route):
            case _:
                View("/home",HomeContent(filePicker)).set(page)
        
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # STARTING PAGE
    page.go("/home")

ft.app(target=main,assets_dir="assets")