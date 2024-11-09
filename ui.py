import tkinter as tk
from tkinter import messagebox
import db_handler

def add_note_window():
    def save_note():
        title = entry_title.get()
        content = entry_content.get("1.0", tk.END)
        category = entry_category.get()
        db_handler.add_note(title, content, category)
        messagebox.showinfo("Success", "Note added successfully!")

    window = tk.Toplevel()
    window.title("Add New Note")

    tk.Label(window, text="Title").pack()
    entry_title = tk.Entry(window)
    entry_title.pack()

    tk.Label(window, text="Content").pack()
    entry_content = tk.Text(window)
    entry_content.pack()

    tk.Label(window, text="Category").pack()
    entry_category = tk.Entry(window)
    entry_category.pack()

    tk.Button(window, text="Save", command=save_note).pack()

def main_window():
    root = tk.Tk()
    root.title("Smart Notes Organizer")

    tk.Button(root, text="Add Note", command=add_note_window).pack()
    tk.Button(root, text="Exit", command=root.quit).pack()

    root.mainloop()

if __name__ == "__main__":
    db_handler.initialize_db()
    main_window()
