import flet as ft
from objects import appWidth,appHeight,baseColor,ElevatedButton,TextField,NavButton
from pytubefix import YouTube
import os
import subprocess

def downloadMp3(url, name):
    if (linkTextField.value and nameTextField.value):
        try:
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

            songStatusText.value = "Success!"
            songStatusText.update()

        except Exception as e:
            songStatusText.value = "Link not valid, try again."
            songStatusText.update()
     
    else:
        songStatusText.value = "Something went wrong, try again."
        songStatusText.update()

    linkTextField.value = ""
    nameTextField.value = ""

    linkTextField.update()
    nameTextField.update()

def HomeContent(filePicker: ft.FilePicker, songFilePicker: ft.FilePicker):
    def submitImage(e):
        if e.files:
            playlistImage.src = e.files[0].path
            playlistImage.update()
    
    def openFilePicker(e):
        filePicker.pick_files()

    def openSongPicker(e):
        songFilePicker.pick_files(allow_multiple=True)
    
    def setSongs(e):
        if e.files:
            songs = [song.name for song in e.files]
            playlistText.value = f"Songs: {", ".join(songs)}"
            playlistText.update()

    filePicker.on_result = submitImage
    songFilePicker.on_result = setSongs

    global linkTextField,nameTextField,playlistImage,songStatusText, playlistFiles
    playlistFiles = []
    songStatusText = ft.Text("",width=350)
    playlistImage = ft.Image(width=150,height=150,src="upload.png")
    linkTextField = TextField("Enter youtube link.",appWidth)
    nameTextField = TextField("Enter name for the downloaded file.",appWidth)
    playlistNameTextField = TextField("Playlist name",appWidth-200)
    playlistText = ft.Text("Songs: ",size=12,width=300)
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Music Player",size=30,weight="bold"),
                ft.Text("Save a Song",size=20,weight="bold"),
                ft.Divider(thickness=2,height=4),
                linkTextField,
                nameTextField,
                ft.Row(
                    controls=[
                        ElevatedButton("Save Song",125, lambda _: downloadMp3(linkTextField.value,nameTextField.value)),
                        songStatusText
                    ]
                ),
                ft.Divider(thickness=2,height=4),
                ft.Text("Create Playlist",size=20,weight="bold"),
                ft.Divider(thickness=2,height=4),
                ft.Row(
                    width=appWidth,
                    controls=[
                        ft.Container(
                            content=playlistImage,
                            on_click= openFilePicker
                        ),
                        ft.Column(
                            controls=[
                                playlistNameTextField,
                                ft.Row(
                                    controls=[
                                        ElevatedButton("Select Songs",140,openSongPicker),
                                        ElevatedButton("Create Playlist",150,None)
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                playlistText
                            ],
                            height=150
                        )
                    ]
                ),
                ft.Divider(thickness=2,height=4),
                ft.Row(width=appWidth,controls=[NavButton("View Playlists",None,appWidth/1.05)],alignment=ft.MainAxisAlignment.CENTER)
            ]
        )
    )

    return content