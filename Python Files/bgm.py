from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def adjust_audio_and_add_music(video_path, audio_path, video_volume=0.5, audio_volume=0.5):
  """
  Adjusts the audio volume of a video and adds a new music track, cutting the added audio to the length of the video.

  Args:
      video_path (str): Path to the input video file.
      audio_path (str): Path to the input audio file.
      video_volume (float, optional): Volume of the video audio (between 0 and 1). Defaults to 0.5.
      audio_volume (float, optional): Volume of the added audio (between 0 and 1). Defaults to 0.5.

  Returns:
      VideoFileClip: The edited video with adjusted audio and added music.
  """

  # Load the video and audio clips
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
audio_path = "bgm/Geng8 (128 kbps).mp3"
video_volume = 0.5
audio_volume = 0.8

edited_video = adjust_audio_and_add_music(video_path, audio_path, video_volume, audio_volume)
edited_video.write_videofile("output_video.mp4")