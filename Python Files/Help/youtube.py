from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os
import yt_dlp
import time

class YoutubeVideoDownloader:
    def __init__(self, link, name):
        self.link = link
        self.video_file_path_webm = 'video.webm'
        self.audio_file_path = 'output_audio.mp3'
        self.output_combined_path = f'{name}.mp4'

    def download(self):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'video.webm',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

    def extract_audio(self):
        video_clip = VideoFileClip(self.video_file_path_webm)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(self.audio_file_path)
        video_clip.close()

    def convert_webm_to_mp4(self):
        video_clip = VideoFileClip(self.video_file_path_webm)
        video_codec = 'libx264'
        video_clip.write_videofile(self.output_combined_path, codec=video_codec, audio_codec='aac')
        video_clip.close()

    def cleanup_temp_files(self):
        # Introduce a delay before attempting to remove the files
        time.sleep(2)  # Adjust the delay as needed

        try:
            os.remove(self.video_file_path_webm)
        except Exception as e:
            print(f"Error while removing video file: {e}")

        try:
            os.remove(self.audio_file_path)
        except Exception as e:
            print(f"Error while removing audio file: {e}")

    def process_video(self):
        self.download()
        self.extract_audio()
        self.convert_webm_to_mp4()
        self.cleanup_temp_files()

if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=2AwAlA3zDdQ"
    name = "example_video"
    downloader = YoutubeVideoDownloader(link, name)
    downloader.process_video()
