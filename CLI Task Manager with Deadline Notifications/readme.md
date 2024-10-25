# CLI Task Manager with Deadline Notifications

This Python project is a simple command-line interface (CLI) task manager that allows users to add, list, delete, and mark tasks as completed. It also sends a desktop notification when a task’s deadline is approaching (within 1 hour). The tasks are saved in a JSON file, allowing persistence across sessions.

## Features

- **Add Tasks**: Add tasks with a name, description, and deadline.
- **List Tasks**: View all tasks along with their deadlines and completion status.
- **Delete Tasks**: Remove a task from the list.
- **Complete Tasks**: Mark tasks as completed.
- **Deadline Notifications**: Receive a desktop notification when a task is nearing its deadline (within 1 hour).
- **Persistent Storage**: Tasks are saved in a JSON file and can be retrieved even after the program is closed and reopened.

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/YourUsername/CLI_Task_Manager.git
cd CLI_Task_Manager
