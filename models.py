# =========
# Classes for objects (Page, Assignment, Modules, Course)
# =========

import json


class Page:
    def __init__(self, raw_data) -> None:
        self.title = raw_data.get("title")
        self.slug = raw_data.get("url")
        self.created_at = raw_data.get("created_at")
        self.body = raw_data.get("body")
        self.raw = raw_data

    def save_json(self, save_path=None):
        if not (save_path):
            save_path = f"./output/Page-{self.slug}.json"

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(self.raw, f, ensure_ascii=False, indent=2)


class Assignment:
    def __init__(self, raw_data) -> None:
        self.title = raw_data.get("name")
        self.id = raw_data.get("id")
        self.created_at = raw_data.get("created_at")
        self.body = raw_data.get("description")
        self.raw = raw_data

    def save_json(self, save_path=None):
        if not (save_path):
            save_path = f"./output/Assignment-{self.id}.json"

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(self.raw, f, ensure_ascii=False, indent=2)
