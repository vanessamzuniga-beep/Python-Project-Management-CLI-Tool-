import json
from pathlib import Path
from models.user import User

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "project_data.json"

def save_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_data():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []



def load_users():
    data = load_data()
    return [User.from_dictionary(user_data) for user_data in data]

def save_users(users):
    data = [user.convert_to_dictionary() for user in users]
    save_data(data)