import mysql.connector
from mysql.connector import Error

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
        print(f"Error: {e}")
        return None

# Add a task to the database
def add_task(task):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        connection.commit()
        print(f"Task '{task}' added successfully!")
        cursor.close()
        connection.close()

# Remove a task from the database
def remove_task(task):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE task = %s", (task,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Task '{task}' removed successfully!")
        else:
            print("Task not found!")
        cursor.close()
        connection.close()

# View all tasks in the database
def view_tasks():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, task FROM tasks")
        tasks = cursor.fetchall()
        if tasks:
            print("\nYour Tasks:")
            for idx, (task_id, task) in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks to show!")
        cursor.close()
        connection.close()

# Main program logic
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
