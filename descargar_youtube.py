import yt_dlp
import os

def descargar_video(url, carpeta_descarga):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': os.path.join(carpeta_descarga, '%(title)s.%(ext)s'),
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def descargar_audio(url, carpeta_descarga):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(carpeta_descarga, '%(title)s.%(ext)s'),
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info).replace('.webm', '.mp3')
