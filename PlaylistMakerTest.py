import flet as ft

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, file_name):
        self.songs.append(file_name)

def main(page: ft.Page):
    page.title = "Playlist Manager"
    
    playlists = {}

    playlist_name_input = ft.TextField(label="Enter Playlist Name", width=300)
    create_button = ft.ElevatedButton("Create Playlist", on_click=lambda e: create_playlist(e, playlist_name_input.value))
    
    
