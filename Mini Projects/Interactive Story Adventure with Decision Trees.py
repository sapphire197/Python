import json
import networkx as nx

# Sample Story Tree in JSON format
story_data = {
    "start": {
        "text": "You are at a crossroads. Do you go left or right?",
        "choices": {
            "left": "forest",
            "right": "mountain"
        }
    },
    "forest": {
        "text": "You enter a dark forest. Do you explore or go back?",
        "choices": {
            "explore": "cave",
            "back": "start"
        }
    },
    "mountain": {
        "text": "You climb the mountain. Do you continue or rest?",
        "choices": {
            "continue": "summit",
            "rest": "camp"
        }
    },
    "cave": {
        "text": "You find a hidden cave. It's dark inside. Do you enter or leave?",
        "choices": {
            "enter": "treasure",
            "leave": "forest"
        }
    },
    "camp": {
        "text": "You set up camp for the night. Do you sleep or stay awake?",
        "choices": {
            "sleep": "nightmare",
            "awake": "mountain"
        }
    },
    "summit": {
        "text": "You reach the summit and see a vast horizon. You've won!",
        "choices": {}
    },
    "treasure": {
        "text": "You find hidden treasure! You've won!",
        "choices": {}
    },
    "nightmare": {
        "text": "You fall into a deep sleep and have a nightmare. You lost.",
        "choices": {}
    }
}

# Hint system
hints = {
    "forest": "The forest hides secrets if you are brave enough to explore.",
    "mountain": "Reaching the summit might bring you great rewards.",
    "cave": "Entering the cave could lead to treasure."
}

def load_game():
    try:
        with open("save_game.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_game(state):
    with open("save_game.json", "w") as f:
        json.dump(state, f)

def display_story(node):
    print(story_data[node]["text"])
    if story_data[node]["choices"]:
        for choice in story_data[node]["choices"]:
            print(f" - {choice}")

def get_hint(node):
    return hints.get(node, "No hints available for this part of the story.")

def play_game():
    state = load_game() or {"current": "start", "score": 0}
    while True:
        current_node = state["current"]
        display_story(current_node)

        if not story_data[current_node]["choices"]:
            print("End of story. Thanks for playing!")
            break

        user_input = input("\nWhat do you want to do? (type 'hint', 'save', or a choice): ").strip().lower()

        if user_input == "hint":
            print(f"Hint: {get_hint(current_node)}\n")
        elif user_input == "save":
            save_game(state)
            print("Game saved!\n")
        elif user_input in story_data[current_node]["choices"]:
            state["current"] = story_data[current_node]["choices"][user_input]
            state["score"] += 10
        else:
            print("Invalid choice. Try again.")

    print(f"Your final score: {state['score']}")

if __name__ == "__main__":
    play_game()
