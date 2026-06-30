import os
import requests
# Optional: from dotenv import load_dotenv; load_dotenv()

api_key = os.getenv("AQ.Ab8RN6JeXqjAGRlkQ5hGShcR1HOF92ZMOlnyKS3dVtNa9y-Szg
")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get("https://amirisgoat597.github.io/catgpt/", headers=headers)
print(response.json())
