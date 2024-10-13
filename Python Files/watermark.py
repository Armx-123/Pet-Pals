from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Define your input and output file names
input_file = "video.mp4"
output_file = "O.mp4"

# Load the video
video = VideoFileClip(input_file)

# Create a TextClip with your custom font
font_path = "Data/DC.otf"
text = "Pet Pals"  # Replace with your desired text

# Create a text clip
text_clip = TextClip(text, fontsize=70, color='transparent', font=font_path, stroke_width=2, stroke_color='black')
text_clip = text_clip.set_position((360)).set_duration(video.duration)
print(TextClip.list('color'))
# Set the position of the text (centered for example)
text_clip = text_clip.set_position('center').set_duration(video.duration)

# Combine the video and text clip
final_video = CompositeVideoClip([video, text_clip])

# Write the result to a file
final_video.write_videofile(output_file, codec='libx264', fps=video.fps)
