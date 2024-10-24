import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Main Tracker Class
class ActivityTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Activity Tracker")
        self.root.geometry("500x400")

        self.activities = []

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

    def add_activity(self):
        activity_name = self.activity_entry.get()
        if activity_name.strip() == "":
            messagebox.showwarning("Input Error", "Please enter an activity name!")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        activity = f"{activity_name} (Added on: {timestamp})"
        self.activities.append(activity)
        self.activity_listbox.insert(tk.END, activity)
        self.activity_entry.delete(0, tk.END)

    def show_activities(self):
        if not self.activities:
            messagebox.showinfo("No Activities", "No activities added yet!")
        else:
            messagebox.showinfo("Activities", "\n".join(self.activities))

# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ActivityTrackerApp(root)
    root.mainloop()
