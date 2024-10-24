# pip install plyer

import json
from datetime import datetime, timedelta
from plyer import notification

# File to store tasks
TASK_FILE = 'tasks.json'

# Load tasks from JSON file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD HH:MM): ")
    deadline_dt = datetime.strptime(deadline, '%Y-%m-%d %H:%M')

    task = {
        'name': task_name,
        'description': description,
        'deadline': deadline,
        'completed': False
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task_name}" added successfully.')

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{idx}. {task['name']} - {task['deadline']} - {status}")
    else:
        print("No tasks available.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    list_tasks()
    task_idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_idx < len(tasks):
        deleted_task = tasks.pop(task_idx)
        save_tasks(tasks)
        print(f'Task "{deleted_task["name"]}" deleted successfully.')
    else:
        print("Invalid task number.")

# Mark a task as completed
def complete_task():
    tasks = load_tasks()
    list_tasks()
    task_idx = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_idx < len(tasks):
        tasks[task_idx]['completed'] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_idx]["name"]}" marked as completed.')
    else:
        print("Invalid task number.")

# Notify user if a task deadline is approaching
def check_deadlines():
    tasks = load_tasks()
    current_time = datetime.now()
    for task in tasks:
        if not task['completed']:
            deadline_dt = datetime.strptime(task['deadline'], '%Y-%m-%d %H:%M')
            if current_time >= deadline_dt - timedelta(hours=1) and current_time < deadline_dt:
                notification.notify(
                    title=f"Task Deadline Approaching: {task['name']}",
                    message=f"Task: {task['description']}\nDeadline: {task['deadline']}",
                    timeout=10
                )

# Main menu
def task_manager():
    print("\nCLI Task Manager\n")
    while True:
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    task_manager()
    check_deadlines()  # Check deadlines every time the program runs
