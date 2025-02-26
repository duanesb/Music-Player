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
    
    def create_playlist(e, name):
        if not name.strip():
            page.snack_bar = ft.SnackBar(ft.Text("Please enter a playlist name"), open=True)
            page.update()
            return
        
        if name in playlists:
            page.snack_bar = ft.SnackBar(ft.Text("Playlist name already exists"), open=True)
            page.update()
            return
        
        playlists[name] = Playlist(name)
        
        playlist_container = ft.Column()
        file_picker = ft.FilePicker(on_result=lambda e, p=name: add_songs(e, p))
        page.overlay.append(file_picker)

        playlist_view = ft.Column([
            ft.Text(name, size=20, weight="bold"),
            ft.ElevatedButton("Upload Songs", on_click=lambda e, p=name: file_picker.pick_files(allow_multiple=True)),
            playlist_container
        ])
        
        playlists[name].view = playlist_container
        page.add(playlist_view)
        playlist_name_input.value = ""  
        page.update()

    def add_songs(e: ft.FilePickerResultEvent, playlist_name):
        if e.files:
            for file in e.files:
                playlists[playlist_name].add_song(file.name)
                playlists[playlist_name].view.controls.append(ft.Text(file.name))
            page.update()

    page.add(playlist_name_input, create_button)
    page.update()

ft.app(target=main)
