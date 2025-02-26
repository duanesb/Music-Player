import flet as ft

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, file_name):
        self.songs.append(file_name)

