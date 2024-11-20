import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import pandas as pd
import os

# Create the main application class
class AcademicPerformanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Academic Performance Tracker")
        self.root.geometry("800x600")
        self.data_file = "data/academic_data.csv"

        # Initialize data storage
        self.data = pd.DataFrame(columns=["Subject", "Grade", "Semester"])

        # Load data if file exists
        self.load_data()

        # Set up GUI
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Academic Performance Tracker", font=("Arial", 18)).pack(pady=10)

        # Buttons for actions
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Add Entry", command=self.add_entry, width=20).grid(row=0, column=0, padx=10)
        tk.Button(frame, text="View Data", command=self.view_data, width=20).grid(row=0, column=1, padx=10)
        tk.Button(frame, text="Visualize Grades", command=self.visualize_data, width=20).grid(row=0, column=2, padx=10)

        # Table for displaying data
        self.tree = ttk.Treeview(self.root, columns=("Subject", "Grade", "Semester"), show="headings")
        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Grade", text="Grade")
        self.tree.heading("Semester", text="Semester")
        self.tree.pack(expand=True, fill="both", pady=10)

        self.update_table()

    def load_data(self):
        if os.path.exists(self.data_file):
            self.data = pd.read_csv(self.data_file)

    def save_data(self):
        os.makedirs("data", exist_ok=True)
        self.data.to_csv(self.data_file, index=False)

    def update_table(self):
        # Clear current data in treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Add new data
        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=(row["Subject"], row["Grade"], row["Semester"]))

    def add_entry(self):
        AddEntryWindow(self)

    def view_data(self):
        self.update_table()

    def visualize_data(self):
        if self.data.empty:
            messagebox.showinfo("No Data", "No data available to visualize.")
            return

        # Group by semester and calculate average grade
        try:
            self.data["NumericGrade"] = self.data["Grade"].astype(float)
            grouped = self.data.groupby("Semester")["NumericGrade"].mean()

            # Plot data
            plt.figure(figsize=(8, 6))
            grouped.plot(kind="bar", color="skyblue")
            plt.title("Average Grades per Semester")
            plt.xlabel("Semester")
            plt.ylabel("Average Grade")
            plt.show()
        except ValueError:
            messagebox.showerror("Error", "Grades must be numeric for visualization.")