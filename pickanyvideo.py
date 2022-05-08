from __future__ import unicode_literals
import youtube_dl

from pytube import YouTube
import os

screen_inst = "Enter the link to your video: "
print(screen_inst)
link = input()




ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([str(link)])


# yt = YouTube(str(link))

# video = yt.streams.filter(only_audio=True).first()

# out_file = video.download(output_path=".")

# base, ext = os.path.splitext(out_file)
# new_file = base + '.wav'
# os.rename(out_file, new_file)










