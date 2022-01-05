"""
Samuel Lee
dlp.py
1/3/2022

utilizes yt-dlp to download youtube videos and process them to mp3's
"""
from yt_dlp import YoutubeDL
from requests import get
from multiprocessing import Pool
import sys


ydl_opts = {
    'format':'250',
    'noplaylist':'True',
    'quiet':'True',
     'postprocessors':[{
         'key':'FFmpegExtractAudio',
         'preferredcodec':'mp3',
         'preferredquality':'192'
     }]}


def download(url):
    with YoutubeDL(ydl_opts) as yt:
        yt.download([url])
    return


def start(urls):
    try:
        todo = []
        for url in urls:
            if url.startswith("https://www.youtube.com/watch?v="):
                todo.append(url)
        with Pool() as p:
            p.map(download, todo)
    except:
        return 1
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        while True:
            urls = input("Enter a url or url's seperated by a space(q to quit): ")
            if urls == "q":
                break
            urls = urls.split(" ")
            start(urls)
    else:
        urls = sys.argv[1:]
        start(urls)