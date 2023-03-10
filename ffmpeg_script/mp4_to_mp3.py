import os
from pathlib import Path

base_dir = path_to_download_folder = str(
    os.path.join(Path.home(), "Downloads/"))
mp4_file = base_dir + "video.mp4"
mp3_file = base_dir + "audio.mp3"
cmd = "ffmpeg -i {} -q:a 0 -map a {}".format(mp4_file, mp3_file)
os.system(cmd)
