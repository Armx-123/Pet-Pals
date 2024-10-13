import os
from moviepy.editor import VideoFileClip

def delete_related_files(base_filename, input_folder):
    """Delete video and audio files related to the base filename."""
    for suffix in ["_video.mp4", "_audio.mp4"]:
        file_path = os.path.join(input_folder, base_filename + suffix)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {file_path} due to the error.")

def standardize_frame_rate(input_folder, output_folder, target_fps):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            try:
                video_clip = VideoFileClip(input_path)
                video_clip = video_clip.set_fps(target_fps)
                video_clip.write_videofile(output_path, codec='libx264')
            except Exception as e:
                print(f"Error processing {input_path}: {e}")
                base_filename = filename.rsplit("_", 1)[0]
                delete_related_files(base_filename, input_folder)

if __name__ == "__main__":
    input_folder = "Videos"
    output_folder = "Videoss"
    target_fps = 30  # Desired frame rate
    
    standardize_frame_rate(input_folder, output_folder, target_fps)
