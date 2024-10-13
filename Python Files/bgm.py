import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def adjust_audio_and_add_random_music(video_path, music_folder, video_volume=0.5, audio_volume=0.5):
    """
    Adjusts the audio volume of a video and adds a randomly selected music track from a folder, 
    cutting the added audio to the length of the video.

    Args:
        video_path (str): Path to the input video file.
        music_folder (str): Path to the folder containing music files.
        video_volume (float, optional): Volume of the video audio (between 0 and 1). Defaults to 0.5.
        audio_volume (float, optional): Volume of the added audio (between 0 and 1). Defaults to 0.5.

    Returns:
        VideoFileClip: The edited video with adjusted audio and added music.
    """

    # List all files in the music folder
    music_files = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]

    # Check if there are any music files in the folder
    if not music_files:
        raise FileNotFoundError("No music files found in the specified folder.")

    # Pick a random music file from the folder
    random_music_file = random.choice(music_files)
    audio_path = os.path.join(music_folder, random_music_file)

    # Load the video and the randomly chosen audio clip
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Adjust the volume of the video audio
    video.audio = video.audio.volumex(video_volume)

    # Adjust the volume of the added audio
    audio = audio.volumex(audio_volume)

    # Ensure added audio doesn't exceed video length
    if audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)

    # Combine the video audio and added audio
    final_audio = CompositeAudioClip([video.audio, audio])

    # Add the final audio to the video
    video = video.set_audio(final_audio)

    return video

# Example usage
video_path = "video.mp4"
music_folder = "bgm"  # Path to the folder containing music files
video_volume = 0.5
audio_volume = 0.8

edited_video = adjust_audio_and_add_random_music(video_path, music_folder, video_volume, audio_volume)
edited_video.write_videofile("output_video.mp4")
