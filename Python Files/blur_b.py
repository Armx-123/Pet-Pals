import cv2
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx.all import resize
import os

# Function to apply soft blur using OpenCV
def apply_soft_blur(frame, blur_intensity):
    # Apply GaussianBlur (soft blur)
    return cv2.GaussianBlur(frame, (blur_intensity, blur_intensity), 0)

# Folder containing videos
input_folder = "Videoss"
output_folder = ""
output_video_name = "blurred_video_with_overlay.mp4"

# Adjustable variables
new_width = 720  # Set the desired width for the final output
new_height = 1280  # Set the desired height for the final output
blur_intensity = 51  # Set the blur intensity (increase for more blur, must be odd)

# List to store processed video clips
processed_clips = []

# Process each video in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):  # You can filter for other video formats too if needed
        file_path = os.path.join(input_folder, filename)
        
        # Load the video file
        clip = VideoFileClip(file_path)
        
        # Resize the clip to fit the specified dimensions (this will be the blurred background)
        stretched_clip = resize(clip, newsize=(new_width, new_height))
        
        # Apply the soft blur effect to each frame using OpenCV
        blurred_clip = stretched_clip.fl_image(lambda frame: apply_soft_blur(frame, blur_intensity))
        
        # Resize the foreground clip while keeping its aspect ratio
        aspect_ratio = clip.w / clip.h
        if new_width / aspect_ratio < new_height:  # Fit based on width
            resized_foreground_clip = resize(clip, width=new_width)
        else:  # Fit based on height
            resized_foreground_clip = resize(clip, height=new_height)

        # Center the foreground clip on top of the blurred background
        foreground_position = (
            (new_width - resized_foreground_clip.w) // 2,
            (new_height - resized_foreground_clip.h) // 2
        )
        
        # Overlay the resized foreground on the blurred background
        final_overlay_clip = CompositeVideoClip([blurred_clip, resized_foreground_clip.set_position(foreground_position)])

        # Append to the processed clips list
        processed_clips.append(final_overlay_clip)

# Concatenate all processed clips into a single video
final_clip = concatenate_videoclips(processed_clips)

# Save the final concatenated video
output_video_path = os.path.join(output_folder, output_video_name)
final_clip.write_videofile(output_video_path, codec="libx264")
