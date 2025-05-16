import json
from pathlib import Path

def save_json(data, filename="data/tariffs.json"):
    """Save data to a JSON file in the data folder."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# from tracker.utils import save_json

# save_json(all_tariffs)
