import os
from Help.reddit import RedditMemeDownloader
from Help.download_reddit import VideoDownloader
from Help.short import VideoShortener
import requests
import random
import time  # Add a small delay to avoid conflicts

TOKEN = 'MTIyNzg5NzY2MjU3MzkwMzg3Mg.G1oFmm.srjPhU-7hg7zqeRZiSNGxZ9ppqeaxuKyKfgIN8'
CHANNEL_ID = '1287789992063664188'
SEND_message_proxy_url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "url-Type": "application/json"
}

def send_message(message):
    if not message.strip():  # Check if the message is empty or contains only whitespace
        return {"error": "Message is empty."}
    data = {
        "content": message
    }
    response = requests.post(SEND_message_proxy_url, headers=headers, json=data)
    return response.json()


def reddit_video(name):
    try:
        names = ["aww", "FunnyAnimals", "AnimalsBeingDerps"]
        subreddit_name = random.choice(names)
        # Create an instance of RedditMemeDownloader
        downloader = RedditMemeDownloader(subreddit_name=subreddit_name, max_merge_count=1)
        # Start downloading meme videos and get the video information list
        video_info_list = downloader.download_meme_videos()

        # Process the video information as needed
        for video_info in video_info_list:
            flair = video_info["flair"]
            video_url = video_info["video_url"]
            audio_url = video_info["audio_url"]
            video_duration = video_info["video_duration"]

            print(flair)
            print(video_url)
            print(audio_url)
            print(video_duration)

            if 0 < int(video_duration) <= 12:
                downloader = VideoDownloader(video_url, audio_url, "Videos/"+name)
                downloader.download_video()
                downloader.combine_audio_video()
                short = VideoShortener("Videos/"+name)
                short.shorten_and_speedup_video()
                return True  # Return True if a video is downloaded
            else :
                send_message("https://v.redd.it/"+video_url)


    except Exception as e:
        print(f"Error in reddit_video function: {e}")

    return False  # Return False if no video is downloaded

downloaded_count = 0
while downloaded_count < 4:
    print(f"Downloaded count: {downloaded_count}")
    functions = [reddit_video]
    # Randomly choose and execute a function
    random_function = random.choice(functions)
    downloaded = random_function(f"video_{downloaded_count}")

    if downloaded:
        downloaded_count += 1