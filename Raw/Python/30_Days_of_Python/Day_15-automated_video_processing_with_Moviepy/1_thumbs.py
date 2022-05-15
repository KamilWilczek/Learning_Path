import os
from moviepy.editor import *
from PIL import Image
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_second_dir = os.path.join(
    SAMPLE_OUTPUTS, "thumbnails-per-half-second"
)
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_per_half_second_dir, exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)

duration = clip.duration
max_duration = int(duration) + 1
for i in range(0, max_duration):
    frame = clip.get_frame(int(i))
    # print(frame) # np.array numpy array # inference
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    # print(f"frame at {i} second saved at {new_img_filepath}")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps * 1.0)

for frame_index, frame in enumerate(clip.iter_frames()):
    # print(frame) # np.array numpy array # inference
    if frame_index % fps == 0:
        current_ms = int((frame_index / fps) * 1000)  # * 1000 gives miliseconds
        new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{current_ms}.jpg")
        # print(f"frame at {frame_index} second saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)

for frame_index, frame in enumerate(clip.iter_frames()):
    fphs = int(fps / 2.0)
    # print(frame) # np.array numpy array # inference
    if frame_index % fphs == 0:
        current_ms = int((frame_index / fps) * 1000)  # * 1000 gives miliseconds
        new_img_filepath = os.path.join(
            thumbnail_per_half_second_dir, f"{current_ms}.jpg"
        )
        # print(f"frame at {frame_index} second saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)
