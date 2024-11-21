# performance_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import fetch_grades

class PerformanceTrendsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Performance Trends")
        self.root.geometry("700x500")

        # Title Label
        self.title_label = tk.Label(self.root, text="Performance Trends", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Frame for selecting options
        self.options_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, bd=2)
        self.options_frame.pack(pady=10, fill=tk.X)

        tk.Label(self.options_frame, text="Select Subject:").grid(row=0, column=0, pady=5, sticky=tk.W)
        self.subject_combobox = ttk.Combobox(self.options_frame, width=30, state="readonly")
        self.subject_combobox.grid(row=0, column=1, pady=5)

        self.show_trend_button = tk.Button(self.options_frame, text="Show Trend", command=self.show_performance_trend)
        self.show_trend_button.grid(row=0, column=2, pady=5, padx=10)

        # Frame for displaying graph
        self.graph_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, bd=2)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        # Load subjects for visualization
        self.load_subjects()

    def load_subjects(self):
        """Loads subjects into the combobox."""
        grades = fetch_grades()
        self.subject_mapping = {grade[1]: grade[0] for grade in grades}
        self.subject_combobox['values'] = list(self.subject_mapping.keys())

    def show_performance_trend(self):
        """Displays the performance trend graph for the selected subject."""
        subject_name = self.subject_combobox.get()

        if not subject_name:
            messagebox.showerror("Input Error", "Please select a subject.")
            return

        subject_id = self.subject_mapping[subject_name]
        grades = fetch_grades()

        # Filter grades for the selected subject
        subject_grades = [(grade[3], grade[2]) for grade in grades if grade[1] == subject_name]
        if not subject_grades:
            messagebox.showinfo("No Data", f"No grades available for '{subject_name}'.")
            return

        # Sort grades by semester
        subject_grades.sort(key=lambda x: x[0])

        semesters = [grade[0] for grade in subject_grades]
        grades_values = [ord(grade[1]) - ord('A') + 4 for grade in subject_grades]  # Convert grades (A=4, B=3, etc.)

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Create Matplotlib figure
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(semesters, grades_values, marker="o", linestyle="-", color="b")
        ax.set_title(f"Performance Trend for {subject_name}")
        ax.set_xlabel("Semester")
        ax.set_ylabel("Grade Points (A=4, B=3, etc.)")
        ax.grid(True)

        # Embed Matplotlib figure into Tkinter
        canvas = FigureCanvasTkAgg(fig, self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = PerformanceTrendsApp(root)
    root.mainloop()

