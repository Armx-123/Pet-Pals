import requests
import json
import os
def get(file,id):
    TOKEN = os.environ['TOKEN']
    DATA_CHANNEL_ID = id

    # Discord API endpoint for fetching messages
    FETCH_MESSAGES_URL = f"https://discord.com/api/v9/channels/{DATA_CHANNEL_ID}/messages"

    # Headers with authorization token and content type
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }

    def fetch_latest_message():
        response = requests.get(FETCH_MESSAGES_URL, headers=headers)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                latest_message = messages[0]  # Assuming the latest message is the first one
                return latest_message
            else:
                print("No messages found in the channel.")
        else:
            print("Failed to fetch messages. Status code:", response.status_code)
        return None

    def save_content_to_json(content, filename=file):
        # Parse the content string as JSON
        content_dict = json.loads(content)
        with open(filename, "w") as file:
            # Serialize the content dictionary without escape sequences
            json.dump(content_dict, file, indent=4)
        print("Content saved to", filename)

    # Fetching the latest message
    latest_message = fetch_latest_message()

    if latest_message:
        # Extracting content and saving it to a JSON file
        content = latest_message.get("content", "")
        save_content_to_json(content)

get("Data/subreddits_data.json","1289201462932406404")
get("Data/part.txt","1289201420960006157")

#"latest_message_content.json"'1232976008408334356'
