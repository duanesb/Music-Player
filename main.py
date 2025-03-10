import flet as ft
import flet_audio as fta
from objects import appWidth,appHeight,baseColor,View
from views.home import HomeContent
from views.playlists import PlaylistsContent
from views.playlists import PlaylistsContent, globalAudio
from views.songViewer import SongViewerContent
import os
import certifi
@@ -27,6 +28,7 @@ def main(page: ft.Page):
    songFilePicker = ft.FilePicker(on_result=handleSongPickerResult)
    page.overlay.append(filePicker)
    page.overlay.append(songFilePicker)
    page.overlay.append(globalAudio) #! Adding playlist audio to the overlay

    # ROUTING
    def route_change(route):