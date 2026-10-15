# =========
# HTTP request to canvas LMS with auth token to get user info and courses list
# =========

import os

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

# vars config
TOKEN = os.getenv("CanvasLMS_token")
DOMAIN = os.getenv("CanvasLMS_domain")
BASE_URL = f"https://{DOMAIN}/api/v1"

# func to iterate through pages to get all data
def get_all(session, url, params=None):
    results = []
    headers = []
    while url:
        r = session.get(url, params=params)
        r.raise_for_status()
        results.extend(r.json())
        headers.extend(r.headers)
        url = r.links.get("next", {}).get("url")
        params = None
    return results, headers

# auth headers and url setup
session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "User-Agent": "Canvas-exporter"
})

# get courses list
courses, _ = get_all(session, f"{BASE_URL}/courses", {"per_page": 100})

print(len(courses))
for c in courses:
    print(f"- {c.get('name', 'Unnamed')} ({c.get('id', 'No ID')})")
