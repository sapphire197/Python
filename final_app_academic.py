# final_app.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import create_tables, add_subject, fetch_subjects, add_grade, fetch_grades
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StudentPerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance Tracker")
        self.root.geometry("800x600")

        # Notebook for tabbed interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Tabs
        self.subject_tab = tk.Frame(self.notebook)
        self.grade_tab = tk.Frame(self.notebook)
        self.trend_tab = tk.Frame(self.notebook)

        self.notebook.add(self.subject_tab, text="Subjects")
        self.notebook.add(self.grade_tab, text="Grades")
        self.notebook.add(self.trend_tab, text="Performance Trends")

        # Initialize tabs
        self.init_subject_tab()
        self.init_grade_tab()
        self.init_trend_tab()

    def init_subject_tab(self):
        """Sets up the Subject Management tab."""
        tk.Label(self.subject_tab, text="Manage Subjects", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.subject_entry = tk.Entry(self.subject_tab, width=40)
        self.subject_entry.pack(pady=5)
        self.add_subject_button = tk.Button(self.subject_tab, text="Add Subject", command=self.add_subject)
        self.add_subject_button.pack(pady=5)

        self.subject_listbox = tk.Listbox(self.subject_tab, width=50, height=15)
        self.subject_listbox.pack(pady=10)
        self.refresh_subject_list()

    def add_subject(self):
        """Adds a subject to the database."""
        subject_name = self.subject_entry.get().strip()
        if not subject_name:
            messagebox.showerror("Input Error", "Subject name cannot be empty.")
            return
        add_subject(subject_name)
        self.subject_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Subject '{subject_name}' added successfully!")
        self.refresh_subject_list()

    def refresh_subject_list(self):
        """Refreshes the subject list."""
        self.subject_listbox.delete(0, tk.END)
        subjects = fetch_subjects()
        for subject in subjects:
            self.subject_listbox.insert(tk.END, subject[1])

    def init_grade_tab(self):
        """Sets up the Grades Management tab."""
        tk.Label(self.grade_tab, text="Manage Grades", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Input Frame
        self.grade_input_frame = tk.Frame(self.grade_tab)
        self.grade_input_frame.pack(pady=10)

        tk.Label(self.grade_input_frame, text="Subject:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.subject_combobox = ttk.Combobox(self.grade_input_frame, width=30, state="readonly")
        self.subject_combobox.grid(row=0, column=1, pady=5)

        tk.Label(self.grade_input_frame, text="Grade:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.grade_entry = tk.Entry(self.grade_input_frame, width=30)
        self.grade_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.grade_input_frame, text="Semester:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.semester_entry = tk.Entry(self.grade_input_frame, width=30)
        self.semester_entry.grid(row=2, column=1, pady=5)

        self.add_grade_button = tk.Button(self.grade_input_frame, text="Add Grade", command=self.add_grade)
        self.add_grade_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Grades Treeview
        self.grades_tree = ttk.Treeview(self.grade_tab, columns=("ID", "Subject", "Grade", "Semester"), show="headings", height=10)
        self.grades_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.grades_tree.heading("ID", text="ID")
        self.grades_tree.heading("Subject", text="Subject")
        self.grades_tree.heading("Grade", text="Grade")
        self.grades_tree.heading("Semester", text="Semester")

        self.refresh_subject_combobox()
        self.display_grades()

    def add_grade(self):
        """Adds a grade to the database."""
        subject_name = self.subject_combobox.get()
        grade = self.grade_entry.get().strip()
        semester = self.semester_entry.get().strip()

        if not subject_name or not grade or not semester:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        subjects = fetch_subjects()
        subject_mapping = {subject[1]: subject[0] for subject in subjects}
        subject_id = subject_mapping[subject_name]

        add_grade(subject_id, grade, semester)
        self.grade_entry.delete(0, tk.END)
        self.semester_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Grade '{grade}' added for '{subject_name}'!")
        self.display_grades()

    def refresh_subject_combobox(self):
        """Refreshes the subject dropdown."""
        subjects = fetch_subjects()
        self.subject_combobox['values'] = [subject[1] for subject in subjects]

    def display_grades(self):
        """Displays grades in the Treeview."""
        for row in self.grades_tree.get_children():
            self.grades_tree.delete(row)

        grades = fetch_grades()
        for grade in grades:
            self.grades_tree.insert("", tk.END, values=grade)

    def init_trend_tab(self):
        """Sets up the Performance Trends tab."""
        tk.Label(self.trend_tab, text="Performance Trends", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.trend_combobox = ttk.Combobox(self.trend_tab, width=40, state="readonly")
        self.trend_combobox.pack(pady=5)

        self.show_trend_button = tk.Button(self.trend_tab, text="Show Trend", command=self.show_performance_trend)
        self.show_trend_button.pack(pady=10)

        self.trend_graph_frame = tk.Frame(self.trend_tab, padx=20, pady=20)
        self.trend_graph_frame.pack(fill=tk.BOTH, expand=True)

        self.refresh_trend_combobox()

    def refresh_trend_combobox(self):
        """Refreshes the combobox for trends."""
        grades = fetch_grades()
        subjects = {grade[1] for grade in grades}
        self.trend_combobox['values'] = list(subjects)

    def show_performance_trend(self):
        """Displays performance trends."""
        subject_name = self.trend_combobox.get()

        if not subject_name:
            messagebox.showerror("Input Error", "Please select a subject.")
            return

        grades = fetch_grades()
        subject_grades = [(grade[3], grade[2]) for grade in grades if grade[1] == subject_name]

        if not subject_grades:
            messagebox.showinfo("No Data", f"No grades available for '{subject_name}'.")
            return

        subject_grades.sort(key=lambda x: x[0])
        semesters = [grade[0] for grade in subject_grades]
        grade_points = [ord(grade[1]) - ord('A') + 4 for grade in subject_grades]

        for widget in self.trend_graph_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(semesters, grade_points, marker="o", color="b")
        ax.set_title(f"Trend for {subject_name}")
        ax.set_xlabel("Semester")
        ax.set_ylabel("Grade Points (A=4, B=3, etc.)")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, self.trend_graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()


if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = StudentPerformanceApp(root)
    root.mainloop()
