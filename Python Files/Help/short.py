import os
from moviepy.editor import VideoFileClip, vfx

class VideoShortener:
    def __init__(self, input_path):
        self.input_path = input_path + ".mp4"
        self.output_path = f"Videos/shortened_{os.path.basename(input_path)}.mp4"  # Use a different name for the output file
        self.target_duration = 10

    def shorten_and_speedup_video(self):
        video_clip = VideoFileClip(self.input_path)
        original_duration = video_clip.duration

        # Check video duration and apply shortening logic
        if original_duration <= self.target_duration:
            print("Video is already equal or less than 10 seconds. Copying to output directory.")
            video_clip.write_videofile(self.output_path, codec='libx264', fps=24)
        elif original_duration <= 15:
            # Shorten to 10 seconds for videos between 10 and 15 seconds
            sped_up_clip = video_clip.fx(vfx.speedx, original_duration / self.target_duration)
            sped_up_clip = sped_up_clip.subclip(0, self.target_duration)
            sped_up_clip.write_videofile(self.output_path, codec='libx264', fps=24)
        else:
            # Shorten to 15 seconds for videos longer than 15 seconds
            sped_up_clip = video_clip.fx(vfx.speedx, original_duration / 15)
            sped_up_clip = sped_up_clip.subclip(0, 15)
            sped_up_clip.write_videofile(self.output_path, codec='libx264', fps=24)

        # Close the video clip to release the file
        video_clip.close()

        # Remove the input file
        os.remove(self.input_path)

if __name__ == "__main__":
    input_path = "video_1"
    target_duration = 10  # Desired duration in seconds

    video_shortener = VideoShortener(input_path)
    video_shortener.shorten_and_speedup_video()
