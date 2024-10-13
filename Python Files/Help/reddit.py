import praw
import os
import json
import time

class RedditMemeDownloader:
    def __init__(self, subreddit_name, max_merge_count=5):
        self.subreddit_name = subreddit_name
        self.max_merge_count = max_merge_count
        self.downloaded_videos = set()
        self.merge_count = 0
        self.last_downloaded_url = self.read_last_downloaded_url()

        self.reddit_instance = praw.Reddit(
            client_id="PX5291z-uAykEUfeaHlGRQ",
            client_secret="oCTu3AvbxtMC7kyg9zqW6VVzsQlLHQ",
            username="Armx11443",
            password="Armxisaboss123",
            user_agent="armx"
        )

    def read_last_downloaded_url(self):
        last_downloaded_url = ""
        data_filename = "Data/subreddits_data.json"
        if os.path.exists(data_filename):
            with open(data_filename, "r") as file:
                data = json.load(file)
                last_downloaded_url = data.get(self.subreddit_name, {}).get('last_downloaded_url', "")
        return "https://v.redd.it/" + last_downloaded_url if last_downloaded_url else ""

    def download_meme_videos(self):
        video_info_list = []

        while self.merge_count < self.max_merge_count:
            try:
                subreddit = self.reddit_instance.subreddit(self.subreddit_name)
                new_posts = subreddit.new(limit=200)

                start_index = 0
                if self.last_downloaded_url:
                    for index, post in enumerate(new_posts):
                        if post and hasattr(post, 'media') and post.media and 'reddit_video' in post.media:
                            video_url = post.media['reddit_video'].get('fallback_url').split("?")[0]
                            if video_url == self.last_downloaded_url:
                                start_index = index + 1
                                break

                for post in list(subreddit.new(limit=200))[start_index:]:
                    if post and hasattr(post, 'media') and post.media and 'reddit_video' in post.media:
                        video_url = post.media['reddit_video'].get('fallback_url').split("?")[0]
                        video_url = video_url.replace("https://v.redd.it/", "")
                        idd = video_url.split("/")[0]
                        audio_url = f"{idd}/DASH_AUDIO_128.mp4"
                        flair = post.link_flair_text if post.link_flair_text else "No Flair"
                        video_duration = post.media['reddit_video']['duration'] if 'duration' in post.media['reddit_video'] else None

                        video_info = {
                            "flair": flair,
                            "video_url": video_url,
                            "audio_url": audio_url,
                            "video_duration": video_duration
                        }

                        video_info_list.append(video_info)

                        if video_url not in self.downloaded_videos:
                            self.downloaded_videos.add(video_url)

                            self.last_downloaded_url = video_url
                            self.save_last_downloaded_url()

                            self.merge_count += 1

                            if self.merge_count >= self.max_merge_count:
                                break

                time.sleep(1)

            except OSError as e:
                print(f"Error: {e}. Skipping to the next URL.")
                continue

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue

        return video_info_list

    def save_last_downloaded_url(self):
        data_filename = "Data/subreddits_data.json"
        data = {}
        if os.path.exists(data_filename):
            with open(data_filename, "r") as file:
                data = json.load(file)

        data[self.subreddit_name] = {'last_downloaded_url': self.last_downloaded_url}

        with open(data_filename, "w") as file:
            json.dump(data, file, indent=4)