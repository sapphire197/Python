# grades_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from database import fetch_subjects, add_grade, fetch_grades

class GradesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grades Management")
        self.root.geometry("600x500")

        # Title Label
        self.title_label = tk.Label(self.root, text="Manage Grades", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Frame for adding grades
        self.add_grade_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, bd=2)
        self.add_grade_frame.pack(pady=10, fill=tk.X)

        tk.Label(self.add_grade_frame, text="Add New Grade", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.add_grade_frame, text="Subject:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.subject_combobox = ttk.Combobox(self.add_grade_frame, width=30, state="readonly")
        self.subject_combobox.grid(row=1, column=1, pady=5)

        tk.Label(self.add_grade_frame, text="Grade:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.grade_entry = tk.Entry(self.add_grade_frame, width=30)
        self.grade_entry.grid(row=2, column=1, pady=5)

        tk.Label(self.add_grade_frame, text="Semester:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.semester_entry = tk.Entry(self.add_grade_frame, width=30)
        self.semester_entry.grid(row=3, column=1, pady=5)

        self.add_grade_button = tk.Button(self.add_grade_frame, text="Add Grade", command=self.add_grade)
        self.add_grade_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame for viewing grades
        self.view_grades_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, bd=2)
        self.view_grades_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Label(self.view_grades_frame, text="Grades List", font=("Helvetica", 12, "bold")).pack(pady=5)

        self.grades_tree = ttk.Treeview(self.view_grades_frame, columns=("ID", "Subject", "Grade", "Semester"), show="headings", height=10)
        self.grades_tree.pack(fill=tk.BOTH, expand=True)

        self.grades_tree.heading("ID", text="ID")
        self.grades_tree.heading("Subject", text="Subject")
        self.grades_tree.heading("Grade", text="Grade")
        self.grades_tree.heading("Semester", text="Semester")

        self.grades_tree.column("ID", width=50)
        self.grades_tree.column("Subject", width=150)
        self.grades_tree.column("Grade", width=100)
        self.grades_tree.column("Semester", width=100)

        # Fetch subjects and grades
        self.load_subjects()
        self.display_grades()

    def load_subjects(self):
        """Load subjects into the combobox."""
        subjects = fetch_subjects()
        self.subject_mapping = {subject[1]: subject[0] for subject in subjects}
        self.subject_combobox['values'] = list(self.subject_mapping.keys())

    def add_grade(self):
        """Handles adding a new grade."""
        subject_name = self.subject_combobox.get()
        grade = self.grade_entry.get().strip()
        semester = self.semester_entry.get().strip()

        if not subject_name or not grade or not semester:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        subject_id = self.subject_mapping[subject_name]
        add_grade(subject_id, grade, semester)
        messagebox.showinfo("Success", f"Grade '{grade}' for '{subject_name}' added successfully!")
        self.grade_entry.delete(0, tk.END)
        self.semester_entry.delete(0, tk.END)
        self.display_grades()

    def display_grades(self):
        """Fetch and display grades in the Treeview."""
        for row in self.grades_tree.get_children():
            self.grades_tree.delete(row)

        grades = fetch_grades()
        for grade in grades:
            self.grades_tree.insert("", tk.END, values=grade)


if __name__ == "__main__":
    root = tk.Tk()
    app = GradesApp(root)
    root.mainloop()
