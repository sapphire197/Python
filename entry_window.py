class AddEntryWindow:
    def __init__(self, parent):
        self.parent = parent
        self.top = tk.Toplevel(parent.root)
        self.top.title("Add Entry")
        self.top.geometry("400x300")

        tk.Label(self.top, text="Add New Entry", font=("Arial", 14)).pack(pady=10)

        # Entry Fields
        frame = tk.Frame(self.top)
        frame.pack(pady=10)

        tk.Label(frame, text="Subject").grid(row=0, column=0, padx=5, pady=5)
        self.subject_entry = tk.Entry(frame)
        self.subject_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Grade").grid(row=1, column=0, padx=5, pady=5)
        self.grade_entry = tk.Entry(frame)
        self.grade_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Semester").grid(row=2, column=0, padx=5, pady=5)
        self.semester_entry = tk.Entry(frame)
        self.semester_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.top, text="Save", command=self.save_entry, width=10).pack(pady=10)
        tk.Button(self.top, text="Cancel", command=self.top.destroy, width=10).pack(pady=5)

    def save_entry(self):
        # Collect data
        subject = self.subject_entry.get()
        grade = self.grade_entry.get()
        semester = self.semester_entry.get()

        # Validate input
        if not subject or not grade or not semester:
            messagebox.showerror("Error", "All fields are required.")
            return

        # Add to parent's data
        new_entry = {"Subject": subject, "Grade": grade, "Semester": semester}
        self.parent.data = self.parent.data.append(new_entry, ignore_index=True)
        self.parent.save_data()
        self.parent.update_table()

        messagebox.showinfo("Success", "Entry added successfully!")
        self.top.destroy()