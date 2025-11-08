# descargar_youtube.py
from yt_dlp import YoutubeDL
import os

def descargar_video(url, carpeta):
    ydl_opts = {
        'outtmpl': os.path.join(carpeta, '%(title)s.%(ext)s'),
        'format': 'mp4'
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        archivo = ydl.prepare_filename(info)
        return os.path.basename(archivo)

def descargar_audio(url, carpeta):
    ydl_opts = {
        'outtmpl': os.path.join(carpeta, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        archivo = ydl.prepare_filename(info)
        archivo = os.path.splitext(archivo)[0] + ".mp3"
        return os.path.basename(archivo)
