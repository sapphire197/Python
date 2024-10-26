import json
import tkinter as tk
from tkinter import messagebox

# Path to store book data
DATA_FILE = 'book_data.json'

# Load books from JSON file
def load_books():
    try:
        with open(DATA_FILE, 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
    return books

# Save books to JSON file
def save_books(books):
    with open(DATA_FILE, 'w') as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    pages = pages_entry.get()

    if not title or not author or not pages.isdigit():
        messagebox.showerror("Error", "Please fill in all fields with valid data.")
        return

    book = {
        'title': title,
        'author': author,
        'total_pages': int(pages),
        'pages_read': 0
    }

    books = load_books()
    books.append(book)
    save_books(books)

    list_books()
    clear_fields()
    messagebox.showinfo("Success", f'Book "{title}" added!')

# Update progress on a book
def update_progress():
    books = load_books()
    selected_book = book_listbox.curselection()

    if not selected_book:
        messagebox.showwarning("Warning", "Please select a book to update progress.")
        return

    pages_read = progress_entry.get()
    if not pages_read.isdigit():
        messagebox.showerror("Error", "Please enter a valid number of pages read.")
        return

    index = selected_book[0]
    books[index]['pages_read'] += int(pages_read)

    if books[index]['pages_read'] > books[index]['total_pages']:
        books[index]['pages_read'] = books[index]['total_pages']

    save_books(books)
    list_books()
    messagebox.showinfo("Success", "Progress updated!")

# Remove a book from the list
def remove_book():
    books = load_books()
    selected_book = book_listbox.curselection()

    if not selected_book:
        messagebox.showwarning("Warning", "Please select a book to remove.")
        return

    index = selected_book[0]
    removed_book = books.pop(index)
    save_books(books)
    list_books()
    messagebox.showinfo("Success", f'Book "{removed_book["title"]}" removed.')

# List all books
def list_books():
    books = load_books()
    book_listbox.delete(0, tk.END)

    for book in books:
        progress = int((book['pages_read'] / book['total_pages']) * 100)
        book_listbox.insert(tk.END, f"{book['title']} by {book['author']} - {progress}% read")

# Clear entry fields
def clear_fields():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    pages_entry.delete(0, tk.END)
    progress_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Book Tracker")
root.geometry("400x500")

# UI Elements
tk.Label(root, text="Title:").pack(pady=5)
title_entry = tk.Entry(root, width=30)
title_entry.pack()

tk.Label(root, text="Author:").pack(pady=5)
author_entry = tk.Entry(root, width=30)
author_entry.pack()

tk.Label(root, text="Total Pages:").pack(pady=5)
pages_entry = tk.Entry(root, width=30)
pages_entry.pack()

tk.Button(root, text="Add Book", command=add_book).pack(pady=10)

tk.Label(root, text="Book List:").pack(pady=5)
book_listbox = tk.Listbox(root, width=50, height=10)
book_listbox.pack()

tk.Label(root, text="Pages Read:").pack(pady=5)
progress_entry = tk.Entry(root, width=30)
progress_entry.pack()

tk.Button(root, text="Update Progress", command=update_progress).pack(pady=10)
tk.Button(root, text="Remove Book", command=remove_book).pack(pady=5)

list_books()  # Display books on launch

root.mainloop()
