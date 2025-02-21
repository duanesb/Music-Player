import flet as ft
from objects import appWidth,appHeight,baseColor
from pytubefix import YouTube

def downloadMp3(url,output):
    yt = YouTube(url)
    audioStream = yt.streams.filter(only_audio=True)
    print(audioStream)
    audioFile = audioStream.download(output)

def HomeContent():
    content = ft.Container(width=appWidth,height=appHeight,
        content=ft.Column(
            controls=[
                ft.Text("Music Player",size=30,weight="bold")
            ]
        )
    )

    downloadMp3("https://www.youtube.com/watch?v=Ssj5ZBuhwIo","assets/songBank")

    return content