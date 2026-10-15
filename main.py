# =========
# HTTP request to canvas LMS with auth token to get user info and courses list
# =========

import os

import requests
from dotenv import load_dotenv
from requests.sessions import Session, session

load_dotenv()

# vars config
TOKEN = os.getenv("CanvasLMS_token")
DOMAIN = os.getenv("CanvasLMS_domain")

# auth headers and url setup
base_url = f"https://{DOMAIN}/api/v1"

session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "User-Agent": "Canvas-exporter"
})

# GET response
response = session.get(f"{base_url}/courses", params={"per_page": 100})

# process response
if response.status_code == 200:
    courses = response.json()
    for i in courses:
        print(f"- {i.get('name', 'Unnamed')} ({i.get('id', 'No ID')})")
else:
    print(response.status_code)
    print(response.text)
