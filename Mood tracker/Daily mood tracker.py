import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import matplotlib.pyplot as plt

# JSON file to store mood entries
DATA_FILE = 'mood_data.json'

# Load mood entries from JSON file
def load_moods():
    try:
        with open(DATA_FILE, 'r') as file:
            moods = json.load(file)
    except FileNotFoundError:
        moods = {}
    return moods

# Save mood entries to JSON file
def save_moods(moods):
    with open(DATA_FILE, 'w') as file:
        json.dump(moods, file, indent=4)

# Add mood entry
def add_mood():
    mood = mood_entry.get()
    date = datetime.now().strftime("%Y-%m-%d")

    if mood:
        moods = load_moods()
        moods[date] = mood
        save_moods(moods)
        messagebox.showinfo("Success", f"Mood for {date} saved!")
        mood_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter your mood.")

# Display mood trend graph
def show_graph():
    moods = load_moods()
    if not moods:
        messagebox.showinfo("Info", "No mood data to display.")
        return

    dates = list(moods.keys())
    mood_values = [int(moods[date]) for date in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, mood_values, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Mood Level (1-10)')
    plt.title('Mood Trend Over Time')
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Daily Mood Tracker")

# UI Elements
tk.Label(root, text="Enter your mood level (1-10):").pack(pady=10)
mood_entry = tk.Entry(root, width=20)
mood_entry.pack()

tk.Button(root, text="Add Mood", command=add_mood).pack(pady=10)
tk.Button(root, text="Show Mood Graph", command=show_graph).pack(pady=10)

root.mainloop()
