import tkinter as tk
from tkinter import messagebox, simpledialog
from db_handler import add_note, get_all_notes, delete_note, initialize_db

def add_new_note():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    category = category_entry.get()

    if not title or not content:
        messagebox.showerror("Error", "Title and content cannot be empty.")
        return

    add_note(title, content, category)
    messagebox.showinfo("Success", "Note added successfully!")
    clear_fields()
    refresh_notes()

def clear_fields():
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    category_entry.delete(0, tk.END)

def refresh_notes():
    notes_listbox.delete(0, tk.END)
    notes = get_all_notes()
    for note in notes:
        notes_listbox.insert(tk.END, f"ID: {note[0]} | Title: {note[1]} | Category: {note[3]}")

def delete_selected_note():
    try:
        selected_note = notes_listbox.get(notes_listbox.curselection())
        note_id = int(selected_note.split('|')[0].split(':')[1].strip())
        delete_note(note_id)
        messagebox.showinfo("Success", "Note deleted successfully!")
        refresh_notes()
    except IndexError:
        messagebox.showerror("Error", "No note selected.")

# Initialize the database
initialize_db()

# Create the main window
root = tk.Tk()
root.title("Smart Notes Organizer")

# Title Entry
tk.Label(root, text="Title").grid(row=0, column=0, sticky='w')
title_entry = tk.Entry(root, width=50)
title_entry.grid(row=0, column=1)

# Content Text Area
tk.Label(root, text="Content").grid(row=1, column=0, sticky='nw')
content_text = tk.Text(root, height=10, width=50)
content_text.grid(row=1, column=1, pady=10)

# Category Entry
tk.Label(root, text="Category").grid(row=2, column=0, sticky='w')
category_entry = tk.Entry(root, width=50)
category_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Note", command=add_new_note).grid(row=3, column=0, pady=10)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=3, column=1)

# Notes Listbox
notes_listbox = tk.Listbox(root, width=80, height=10)
notes_listbox.grid(row=4, column=0, columnspan=2, pady=20)
refresh_notes()

# Delete Note Button
tk.Button(root, text="Delete Selected Note", command=delete_selected_note).grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
