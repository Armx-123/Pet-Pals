import os
import requests
from moviepy.editor import VideoFileClip, AudioFileClip

class VideoDownloader:
    def __init__(self, video_url, audio_url, output_path):
        self.video_url = "https://v.redd.it/"+video_url
        self.audio_url = "https://v.redd.it/"+audio_url
        self.output_path = output_path

    def download_video(self):
        # Download video
        video_response = requests.get(self.video_url, stream=True)
        with open(self.output_path + "_video.mp4", 'wb') as video_file:
            for chunk in video_response.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)

        # Download audio
        audio_response = requests.get(self.audio_url, stream=True)
        with open(self.output_path + "_audio.mp4", 'wb') as audio_file:
            for chunk in audio_response.iter_content(chunk_size=1024):
                if chunk:
                    audio_file.write(chunk)

        print(f"Videos downloaded successfully to {self.output_path}_video.mp4 and {self.output_path}_audio.mp4")

    def combine_audio_video(self):
        video_clip = VideoFileClip(self.output_path + "_video.mp4")
        audio_clip = AudioFileClip(self.output_path + "_audio.mp4")

        # Set the audio of the video clip to the downloaded audio clip
        video_clip = video_clip.set_audio(audio_clip)

        # Write the final combined video with audio
        output_file_path = self.output_path + ".mp4"
        video_clip.write_videofile(output_file_path, codec="libx264", audio_codec="aac")

        print(f"Combined video and audio saved successfully to {output_file_path}")

        # Delete temporary files
        os.remove(self.output_path + "_video.mp4")
        os.remove(self.output_path + "_audio.mp4")
        print("Temporary files deleted.")

if __name__ == "__main__":
    # Example usage
    video_url = "https://v.redd.it/kc58zm36i42c1/DASH_480.mp4"
    audio_url = "https://v.redd.it/kc58zm36i42c1/DASH_AUDIO_128.mp4"
    output_path = "downloaded_video"

    downloader = VideoDownloader(video_url, audio_url, output_path)
    downloader.download_video()
    downloader.combine_audio_video()
link ="https://sd.rapidsave.com/download.php?permalink=https://www.reddit.com/r/MemeVideos/comments/1824rxs/you_got_the_guts/&video_url=https://v.redd.it/kc58zm36i42c1/DASH_480.mp4?source=fallback&audio_url=https://v.redd.it/kc58zm36i42c1/DASH_AUDIO_128.mp4"