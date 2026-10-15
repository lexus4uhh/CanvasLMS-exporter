# =========
# Class for data collection from CanvasLMS
# =========

import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv(override=True)


class Collector:
    def __init__(self) -> None:
        self.TOKEN = os.getenv("CanvasLMS_token")
        self.DOMAIN = os.getenv("CanvasLMS_domain")
        self.BASE_URL = f"https://{self.DOMAIN}/api/v1"

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.TOKEN}",
                "Accept": "application/json",
                "User-Agent": "Canvas-exporter",
            }
        )

    def _get_all(self, url, params=None):
        results = []
        headers = []
        while url:
            r = self.session.get(url, params=params)
            r.raise_for_status()
            results.extend(r.json())
            headers.extend(r.headers)
            url = r.links.get("next", {}).get("url")
            params = None
        return results, headers

    def _to_api(self, user_url: str) -> str:
        u = urlparse(user_url)
        return f"https://{u.netloc}/api/v1{u.path}" + (f"?{u.query}" if u.query else "")

    def collect(self, url, params=None):
        api_url = self._to_api(url)
        result = self.session.get(api_url, params=params)

        return {
            "json": result.json(),
            "status": result.status_code,
            "headers": result.headers,
        }
