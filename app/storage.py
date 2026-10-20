import json
from pathlib import Path


def load_items(path):
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Format data inventaris tidak valid.")

    return data


def save_items(items, path):
    with path.open("w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=2)