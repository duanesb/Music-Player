import flet as ft
from objects import appWidth,appHeight,baseColor,View
from views.home import HomeContent
<<<<<<< HEAD
from views.playlists import PlaylistsContent, globalAudio #! Included the audio object created in playlist view to add it to the page overlay
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
=======
from views.playlists import PlaylistsContent
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

def filePickerResult(e:ft.FilePickerResultEvent):
    if e.files:
        path = e.files[0].path

def handleSongPickerResult(e):
    if e.files:
        paths = [file.path for file in e.files]

>>>>>>> parent of 48fed34 (Fixes)
def main(page: ft.Page):
    # CONFIG
    page.title = "Music Player"
    page.window.width = appWidth
    page.window.height = appHeight
<<<<<<< HEAD
=======

>>>>>>> parent of 48fed34 (Fixes)
    # FILE PICKER
    filePicker = ft.FilePicker(on_result=filePickerResult)
    songFilePicker = ft.FilePicker(on_result=handleSongPickerResult)
    page.overlay.append(filePicker)
    page.overlay.append(songFilePicker)
<<<<<<< HEAD
    page.overlay.append(globalAudio) #! Adding playlist audio to the overlay
=======

>>>>>>> parent of 48fed34 (Fixes)
    # ROUTING
    def route_change(route):
        page.views.clear()
        match(page.route):
<<<<<<< HEAD
            case "/songViewer":
                View("/songViewer",SongViewerContent()).set(page)
=======
>>>>>>> parent of 48fed34 (Fixes)
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
<<<<<<< HEAD
    # STARTING PAGE
    page.go("/home")
ft.app(target=main,assets_dir="assets")
=======

    # STARTING PAGE
    page.go("/home")

ft.app(target=main,assets_dir="assets")
>>>>>>> parent of 48fed34 (Fixes)
