from pytube import Search, YouTube
import os
from pathlib import Path

res = input("Search on youtube : ")

s = Search(res)
print(f"Nbr results : {len(s.results)}")
for res in s.results:
    print(res.title)
    # print(res.description)
    print(res.channel_url)
    print(res.video_id)

url = YouTube(f"https://www.youtube.com/watch?v={s.results[0].video_id}")

print("Downloading first video...🍱")

video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)

print("Video Downloaded !! ✅")
