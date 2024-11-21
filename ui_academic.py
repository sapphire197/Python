# ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db, add_subject, fetch_subjects

# Initialize the database
connect_db()

class AcademicTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Academic Performance Tracker")
        self.root.geometry("600x400")

        # Title Label
        self.title_label = tk.Label(self.root, text="Academic Performance Tracker", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Frame for adding subjects
        self.add_subject_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, bd=2)
        self.add_subject_frame.pack(pady=10, fill=tk.X)

        tk.Label(self.add_subject_frame, text="Add New Subject", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.add_subject_frame, text="Subject Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.subject_name_entry = tk.Entry(self.add_subject_frame, width=30)
        self.subject_name_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.add_subject_frame, text="Credit Hours:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.credit_hours_entry = tk.Entry(self.add_subject_frame, width=10)
        self.credit_hours_entry.grid(row=2, column=1, pady=5)

        self.add_subject_button = tk.Button(self.add_subject_frame, text="Add Subject", command=self.add_subject)
        self.add_subject_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame for viewing subjects
        self.view_subject_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, bd=2)
        self.view_subject_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Label(self.view_subject_frame, text="Subjects List", font=("Helvetica", 12, "bold")).pack(pady=5)

        self.subject_tree = ttk.Treeview(self.view_subject_frame, columns=("ID", "Subject Name", "Credit Hours"), show="headings", height=10)
        self.subject_tree.pack(fill=tk.BOTH, expand=True)

        self.subject_tree.heading("ID", text="ID")
        self.subject_tree.heading("Subject Name", text="Subject Name")
        self.subject_tree.heading("Credit Hours", text="Credit Hours")

        self.subject_tree.column("ID", width=50)
        self.subject_tree.column("Subject Name", width=200)
        self.subject_tree.column("Credit Hours", width=100)

        # Fetch and display subjects
        self.display_subjects()

    def add_subject(self):
        """Handles adding a new subject."""
        subject_name = self.subject_name_entry.get().strip()
        credit_hours = self.credit_hours_entry.get().strip()

        if not subject_name or not credit_hours:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            credit_hours = int(credit_hours)
            add_subject(subject_name, credit_hours)
            messagebox.showinfo("Success", f"Subject '{subject_name}' added successfully!")
            self.subject_name_entry.delete(0, tk.END)
            self.credit_hours_entry.delete(0, tk.END)
            self.display_subjects()
        except ValueError:
            messagebox.showerror("Input Error", "Credit hours must be a valid number.")

    def display_subjects(self):
        """Fetches and displays subjects in the Treeview."""
        for row in self.subject_tree.get_children():
            self.subject_tree.delete(row)

        subjects = fetch_subjects()
        for subject in subjects:
            self.subject_tree.insert("", tk.END, values=subject)


if __name__ == "__main__":
    root = tk.Tk()
    app = AcademicTrackerApp(root)
    root.mainloop()
