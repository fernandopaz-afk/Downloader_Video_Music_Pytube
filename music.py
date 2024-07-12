from pytube.cli import on_progress
from pytube import YouTube

url = input("Ingrese el audio a descargar por favor: ")

try:
    video = YouTube(url, on_progress_callback=on_progress)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f"{video.title}.mp3")
    
    file_size_mb = stream.filesize / 1024 / 1024
    
    print(f"Title: {video.title}")
    print(f"Size: {file_size_mb:.2f} MB")
    print("The video is downloaded in MP3 format")
except KeyError:
    print("Unable to fetch video information. Please check the video URL or your network connection.")
except Exception as e:
    print(f"An error occurred: {e}")
