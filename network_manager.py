# network_manager.py
import json
import os

# Instead of the internet, we use two local files in your project folder
WORDS_FILE = "global_database_words.json"
CHOSEN_FILE = "global_database_chosen.json"

def get_cloud_words():
    """Fetches the global list of words from a local JSON file."""
    if not os.path.exists(WORDS_FILE):
        return [] # Return empty list if file doesn't exist yet
    try:
        with open(WORDS_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception as e:
        print(f"Error reading local database: {e}")
        return []

def save_cloud_words(word_list):
    """Overwrites the global list in the local JSON file."""
    try:
        with open(WORDS_FILE, "w") as f:
            json.dump(word_list, f)
        return True
    except Exception as e:
        print(f"Error saving to local database: {e}")
        return False

def get_current_chosen_word():
    """Fetches the active word that was chosen randomly from the local file."""
    if not os.path.exists(CHOSEN_FILE):
        return None
    try:
        with open(CHOSEN_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return None

def set_current_chosen_word(word):
    """Saves the chosen random word locally so all other running windows see it."""
    try:
        with open(CHOSEN_FILE, "w") as f:
            json.dump(word, f)
        return True
    except Exception:
        return False
