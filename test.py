from pytubefix import YouTube
import os
 
def downloadMp3(url,destination,name):
    yt = YouTube(url)
    audioStream = yt.streams.filter(only_audio=True).first()

    # DOWNLOADS THE AUDIO FILE
    audioFile = audioStream.download(output_path=destination,filename=f"{name}.mp3")

downloadMp3("https://www.youtube.com/watch?v=Ssj5ZBuhwIo","assets/songBank","test")