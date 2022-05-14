import os
from pydoc import cli
from moviepy.editor import *
from PIL import Image
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
os.makedirs(thumbnail_dir, exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)

duration = clip.duration
max_duration = int(duration) + 1
for i in range(0, max_duration):
    print(f"frame at {i} second")
    frame = clip.get_frame(int(i))
    # print(frame)
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)
