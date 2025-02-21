import flet as ft
from objects import appWidth,appHeight,baseColor,ElevatedButton
from pytubefix import YouTube
import os
import subprocess

def downloadMp3(url, name):
    yt = YouTube(url)
    audioStream = yt.streams.filter(only_audio=True).first()
    downloadedFile = audioStream.download(output_path="assets/songBank")
    
    # DOWNLOAD THE FILE AS MP3 (NOT AS AN MP3 THOUGH)
    mp3_filename = os.path.join("assets/songBank", f"{name}.mp3")
    
    # FFMPEG Conversion to MP3
    command = [
        "ffmpeg",
        "-y",               # Overwrite output file if it exists
        "-i", downloadedFile,
        "-vn",              # Disable video
        "-ar", "44100",     # Set audio sampling rate
        "-ac", "2",         # Set number of audio channels
        "-b:a", "192k",     # Set audio bitrate
        mp3_filename
    ]
    
    subprocess.run(command, check=True)
    os.remove(downloadedFile)


def HomeContent():
    linkTextField = ft.TextField(label="Enter Youtube Link")
    nameTextField = ft.TextField(label="Enter Name for File")
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Music Player",size=30,weight="bold"),
                ft.Text("Save a Song",size=20,weight="bold"),
                linkTextField,
                nameTextField,
                ElevatedButton("Save Song",None),
                ft.Text("Create Playlist",size=20,weight="bold"),
            ]
        )
    )

    return content