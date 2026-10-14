# =========
# HTTP request to canvas LMS with auth token to get user info and courses list
# =========

import os

import requests
from dotenv import load_dotenv

load_dotenv()

# vars config
TOKEN = os.getenv("CanvasLMS_token")
DOMAIN = os.getenv("CanvasLMS_domain")

# auth headers and url setup
url = f"https://{DOMAIN}/api/v1/courses"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json"
}

# GET response
response = requests.get(url, headers=headers)

# process response
if response.status_code == 200:
    courses = response.json()
    for i in courses:
        print(f"- {i.get('name', 'Unnamed')} ({i.get('id', 'No ID')})")
else:
    print(response.status_code)
    print(response.text)
