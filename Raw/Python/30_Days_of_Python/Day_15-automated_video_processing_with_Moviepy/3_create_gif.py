import os
from moviepy.editor import *
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.video.fx.all import crop


source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)
output_path_1 = os.path.join(GIF_DIR, "sample_1.gif")
output_path_2 = os.path.join(GIF_DIR, "sample_2.gif")

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10, 20)
subclip = subclip.resize(width=320)
subclip.write_gif(output_path_1, fps=20, program="ffmpeg")

w, h = clip.size
subclip2 = clip.subclip(10, 20)
squared_cropped_clip = crop(
    subclip2, width=320, height=320, x_center=w / 2, y_center=h / 2
)
squared_cropped_clip.write_gif(output_path_2, fps=fps, program="ffmpeg")
