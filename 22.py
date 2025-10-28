import scrapetube
import yt_dlp
from tkinter import *
import os

hannel_id = 'UCIyLQ6cL0eWj1jT6oyy148w'
lnk1 = f"https://www.youtube.com/watch?v={hannel_id}"


video_url = lnk1  # +video_id
#     # video_url="https://www.youtube.com/watch?v="+video_id
# URLS = [video_url]
ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'ffmpeg_location': os.path.realpath('C:\\prog\\ffmpeg\\bin\\ffmpeg.exe'),
    'outtmpl': 'cache/%(title)s.%(ext)s',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

# dl_opts = {
#         "format": "m4a/bestaudio/worst",
#         "outtmpl": "cache/%(id)s.%(ext)s",
#         "keepvideo": False,
#         "noplaylist": True,
#         "continue_dl": True,
#         "verbose": False,
#         "quiet": False,
#         "noprogress": True,
#     }

ydl = yt_dlp.YoutubeDL(ydl_opts)

try:
    vidstr = scrapetube.get_channel(hannel_id, limit=1, content_type="videos")
    videos = [*vidstr,]
    vd1 = [*vidstr,]
    videos = [{"id": v["videoId"], "url": lnk1+v['videoId']} for v in videos]
except Exception as e:
    print(e)
    # exit(0)

for video in videos:
    video_id, video_url = video["id"], video["url"]

try:
    video_info = ydl.extract_info(video_url, download=False)
except Exception as e:
    print(e)

# Пропускаем стримы которые еще в эфире
# print(video_info.get("is_live", None))
print(videos)

print('--', vd1)


numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10,
           4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
print(result)
