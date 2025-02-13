import json
import random
import os

# Load the JSON file
JSON_FILE = "japanese_phrases.json"

def load_phrases(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def display_random_phrase(phrases):
    phrase = random.choice(phrases)
    print("\nRandom Japanese Phrase:")
    print(f"English: {phrase['English']}")
    print(f"Japanese: {phrase['Japanese']}")
    print(f"Pronunciation: {phrase['Pronunciation']}")

    print("\nPress any key to exit...")
    os.system("pause" if os.name == "nt" else "read -n 1 -s")

if __name__ == "__main__":
    phrases = load_phrases(JSON_FILE)
    display_random_phrase(phrases)
