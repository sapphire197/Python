import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

# Full path to the activities.json file
ACTIVITY_FILE = r'C:\Users\Alagammai\Alagu\Projects\Github\Python\Python\Activities_Tracker\activities.json'

# Load activities from the file if it exists
def load_activities():
    if os.path.exists(ACTIVITY_FILE):
        with open(ACTIVITY_FILE, 'r') as file:
            return json.load(file)
    return []

# Save activities to the file
def save_activities(activities):
    with open(ACTIVITY_FILE, 'w') as file:
        json.dump(activities, file, indent=4)

# Main Tracker Class
class ActivityTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Activity Tracker")
        self.root.geometry("500x400")

        # Load existing activities from file
        self.activities = load_activities()

        # Label
        self.title_label = tk.Label(root, text="Activity Tracker", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Activity Entry
        self.activity_label = tk.Label(root, text="Enter Activity Name:", font=("Arial", 12))
        self.activity_label.pack(pady=5)

        self.activity_entry = tk.Entry(root, font=("Arial", 12))
        self.activity_entry.pack(pady=5)

        # Add Activity Button
        self.add_button = tk.Button(root, text="Add Activity", command=self.add_activity, font=("Arial", 12))
        self.add_button.pack(pady=5)

        # Display Activities Button
        self.show_button = tk.Button(root, text="Show All Activities", command=self.show_activities, font=("Arial", 12))
        self.show_button.pack(pady=5)

        # Activity List Display Area
        self.activity_listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 12))
        self.activity_listbox.pack(pady=10)

        # Load existing activities into the listbox
        self.load_activities_into_listbox()

    def load_activities_into_listbox(self):
        """Load existing activities into the Listbox."""
        for activity in self.activities:
            activity_str = f"{activity['name']} (Added on: {activity['timestamp']})"
            self.activity_listbox.insert(tk.END, activity_str)

    def add_activity(self):
        activity_name = self.activity_entry.get()
        if activity_name.strip() == "":
            messagebox.showwarning("Input Error", "Please enter an activity name!")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        activity = {"name": activity_name, "timestamp": timestamp}
        
        # Add the new activity to the list and save it to the file
        self.activities.append(activity)
        save_activities(self.activities)

        # Update the Listbox
        activity_str = f"{activity_name} (Added on: {timestamp})"
        self.activity_listbox.insert(tk.END, activity_str)
        self.activity_entry.delete(0, tk.END)

    def show_activities(self):
        if not self.activities:
            messagebox.showinfo("No Activities", "No activities added yet!")
        else:
            activity_strs = [f"{activity['name']} (Added on: {activity['timestamp']})" for activity in self.activities]
            messagebox.showinfo("Activities", "\n".join(activity_strs))

# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ActivityTrackerApp(root)
    root.mainloop()
