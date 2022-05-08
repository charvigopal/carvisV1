from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=uWRmBjFxttc'])

# Code Source: https://stackoverflow.com/questions/40713268/download-youtube-video-using-python-to-a-certain-directory 