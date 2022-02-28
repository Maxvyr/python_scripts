import pytube 
import os
from pathlib import Path

link = input('Enter Youtube Video URL')
url = pytube.YouTube(link)
print("downloading start ....")


video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print('downloaded', link)