import flet as ft
import flet_audio as fta
from objects import appWidth,appHeight,baseColor,View
from views.home import HomeContent
from views.playlists import PlaylistsContent, globalAudio
from views.songViewer import SongViewerContent
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

def filePickerResult(e:ft.FilePickerResultEvent):
    if e.files:
        path = e.files[0].path

def handleSongPickerResult(e):
    if e.files:
        paths = [file.path for file in e.files]

def main(page: ft.Page):
    # CONFIG
    page.title = "Music Player"
    page.window.width = appWidth
    page.window.height = appHeight

    # FILE PICKER
    filePicker = ft.FilePicker(on_result=filePickerResult)
    songFilePicker = ft.FilePicker(on_result=handleSongPickerResult)
    page.overlay.append(filePicker)
    page.overlay.append(songFilePicker)
    page.overlay.append(globalAudio) #! Adding playlist audio to the overlay

    # ROUTING
    def route_change(route):
        page.views.clear()
        match(page.route):
            case "/songViewer":
                View("/songViewer",SongViewerContent()).set(page)
            case "/playlists":
                View("/playlists",PlaylistsContent()).set(page)
            case _:
                View("/home",HomeContent(filePicker,songFilePicker)).set(page)
        
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