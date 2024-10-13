import requests
import json
import os

def mess(file,id):
    TOKEN = os.environ['TOKEN']
    DATA_CHANNEL_ID = id


    # Discord API endpoint for sending messages
    SEND_MESSAGE_URL = f"https://discord.com/api/v9/channels/{DATA_CHANNEL_ID}/messages"

    # Discord API endpoint for editing messages
    EDIT_MESSAGE_URL = f"https://discord.com/api/v9/channels/{DATA_CHANNEL_ID}/messages"

    # Headers with authorization token and content type
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }

    def send_message(message):
        data = {
            "content": message
        }
        response = requests.post(SEND_MESSAGE_URL, headers=headers, json=data)
        return response.json()

    def edit_message(message_id, new_content):
        data = {
            "content": new_content
        }
        url = f"{EDIT_MESSAGE_URL}/{message_id}"
        response = requests.patch(url, headers=headers, json=data)
        return response.json()

    def read_content_from_json(filename=file):
        with open(filename, "r") as file:
            content = json.load(file)
        return content

    # Fetching the latest message ID
    response = requests.get(SEND_MESSAGE_URL, headers=headers)
    if response.status_code == 200:
        messages = response.json()
        if messages:  # If there are messages in the channel
            latest_message_id = messages[0]['id']  # Assuming the latest message is the first in the list
            message_content = read_content_from_json()
            # Editing the latest message with the content from the JSON file
            response = edit_message(latest_message_id, json.dumps(message_content))
            print("Message edited:", response)
        else:  # If there are no messages in the channel
            message_content = read_content_from_json()
            # Send the message instead
            response = send_message(json.dumps(message_content))
            print("Message sent:", response)
    else:
        print("Failed to fetch messages.")

mess("Data/subreddits_data.json","1289201462932406404")
mess("Data/part.txt","1289201420960006157")
