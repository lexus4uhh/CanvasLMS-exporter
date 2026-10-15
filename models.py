# =========
# Classes for objects (Page, Assignment, Modules, Course)
# =========


class Page:
    def __init__(self, raw_data) -> None:
        self.title = raw_data.get("title")
        self.slug = raw_data.get("url")
        self.created_at = raw_data.get("created_at")
        self.body = raw_data.get("body")
        self.raw = raw_data


class Assignment:
    def __init__(self, raw_data) -> None:
        self.title = raw_data.get("name")
        self.id = raw_data.get("id")
        self.created_at = raw_data.get("created_at")
        self.body = raw_data.get("description")
        self.raw = raw_data
