import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

# Establish connection to MySQL
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host if different
            database='todo_db',  # Name of your database
            user='root',  # Your MySQL username
            password='PASSWORD'  # Your MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Error", f"Database connection error: {e}")
        return None

# Add a task to the database
def add_task():
    task = task_entry.get()
    if task:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", f"Task '{task}' added successfully!")
            task_entry.delete(0, tk.END)
            view_tasks()  # Refresh the task list
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Remove a task from the database
def remove_task():
    task = task_entry.get()
    if task:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM tasks WHERE task = %s", (task,))
            connection.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Task '{task}' removed successfully!")
            else:
                messagebox.showwarning("Error", "Task not found!")
            cursor.close()
            connection.close()
            task_entry.delete(0, tk.END)
            view_tasks()  # Refresh the task list
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# View all tasks in the database
def view_tasks():
    task_listbox.delete(0, tk.END)  # Clear the listbox before populating
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT task FROM tasks")
        tasks = cursor.fetchall()
        if tasks:
            for task in tasks:
                task_listbox.insert(tk.END, task[0])
        else:
            task_listbox.insert(tk.END, "No tasks to show!")
        cursor.close()
        connection.close()

# Set up the GUI using Tkinter
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Task input field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons for Add, Remove, and View Tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Task list display
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Refresh button to view tasks
view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack(pady=5)

# Start with a list of tasks already loaded
view_tasks()

# Run the Tkinter event loop
root.mainloop()
