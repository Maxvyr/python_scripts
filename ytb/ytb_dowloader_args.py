from pytube import YouTube
import os
from pathlib import Path
from sys import argv


link = argv[1]
url = YouTube(link)
print("downloading start ....")


video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print('downloaded', link)
