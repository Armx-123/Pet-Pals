# main.py

from Help.reddit import RedditMemeDownloader

def main():
    # Specify the subreddit name and maximum merge count
    subreddit_name = "MemeVideos"
    max_merge_count = 1

    # Create an instance of RedditMemeDownloader
    downloader = RedditMemeDownloader(subreddit_name=subreddit_name, max_merge_count=max_merge_count)

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
        print(video_duration)# Do something with the video information (e.g., store in separate variables)

if __name__ == "__main__":
    main()
