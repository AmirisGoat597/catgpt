import os
import requests
# Optional: from dotenv import load_dotenv; load_dotenv()

api_key = os.getenv("fish_f572a80be57c61a26a4f5875b4a9040781abc59cb0c183285babd656b701aeb5")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get("https://amirisgoat597.github.io/catgpt/", headers=headers)
print(response.json())
