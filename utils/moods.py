import json
from pathlib import Path

USERS_FILE = Path("storage/users.json")
if not USERS_FILE.exists():
    USERS_FILE.write_text("{}")

def get_user_mood(user_id):
    users = json.loads(USERS_FILE.read_text())
    return users.get(str(user_id), {}).get("mood", "neutral")

def set_user_mood(user_id, mood):
    users = json.loads(USERS_FILE.read_text())
    if str(user_id) not in users:
        users[str(user_id)] = {}
    users[str(user_id)]["mood"] = mood
    USERS_FILE.write_text(json.dumps(users, indent=2))
