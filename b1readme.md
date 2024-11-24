# **Task Management System for College Students**

This **Task Management System** is a web-based application designed to help college students manage their academic and personal tasks, set deadlines, and receive reminders and notifications. The application will allow students to create, edit, delete, and view tasks, with each task having an associated deadline and reminder.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Setup and Installation](#setup-and-installation)
5. [Backend - Flask API](#backend-flask-api)
6. [Frontend - User Interface](#frontend-user-interface)
7. [Database Setup (MySQL)](#database-setup-mysql)
8. [Reminder and Notification System](#reminder-and-notification-system)
9. [Running the Application](#running-the-application)
10. [Contributing](#contributing)
11. [License](#license)

---

## **Project Overview**

The **Task Management System** provides a solution to help college students organize their daily tasks, assignments, exam schedules, and personal reminders. It provides the following features:

- Create tasks with specific deadlines.
- Set reminders for tasks (e.g., reminders for assignments or exam preparations).
- View, update, and delete tasks.
- Receive notifications when tasks are nearing their deadlines.

This application uses **Flask** for the backend, **MySQL** for the database, and a clean **HTML/CSS/JavaScript** frontend for a smooth user interface.

---

## **Technologies Used**

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Scheduler**: Python `schedule` library
- **Notification**: Flask mail for email notifications and playsound for alarm sounds

---

## **Features**

1. **Task Creation**: Add new tasks with title, description, and deadlines.
2. **Task Updates**: Edit or update tasks as per the requirement.
3. **Task Deletion**: Delete tasks that are completed or canceled.
4. **Task Reminders**: Set alerts for tasks that notify the user before the deadline.
5. **View Tasks**: View all tasks sorted by deadline.
6. **Deadline Notifications**: Get a sound alarm or email notifications as reminders.
7. **Mobile Responsive**: User interface designed for mobile and desktop.

---

## **Setup and Installation**

### **Prerequisites**

- Python 3.x
- MySQL Server
- Flask
- MySQL Connector for Python
- JavaScript and browser

### **Step 1: Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/task-management-system.git
cd task-management-system
```

### **Step 2: Install Dependencies**

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### **Step 3: Set Up MySQL Database**

1. Open MySQL Command Line or MySQL Workbench.
2. Create the database:

   ```sql
   CREATE DATABASE task_manager;
   ```

3. Create the table to store tasks:

   ```sql
   CREATE TABLE tasks (
       task_id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT NOT NULL,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       deadline DATETIME NOT NULL,
       reminder_time DATETIME NOT NULL,
       status ENUM('pending', 'completed') DEFAULT 'pending',
       FOREIGN KEY (user_id) REFERENCES users(user_id)
   );
   ```

4. Configure your MySQL connection in `app.py`:

   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'your-password'
   app.config['MYSQL_DB'] = 'task_manager'
   ```

---

## **Backend - Flask API**

The backend is built using Flask and is responsible for handling the CRUD operations (Create, Read, Update, Delete) for tasks, along with the logic for sending reminders.

### **Routes**:

- **GET /tasks**: Fetch all tasks for the user.
- **POST /tasks**: Create a new task.
- **PUT /tasks/<task_id>**: Update a task.
- **DELETE /tasks/<task_id>**: Delete a task.

### Example: Creating a New Task via POST Request

```python
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data['title']
    description = data['description']
    deadline = data['deadline']
    reminder_time = data['reminder_time']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO tasks (title, description, deadline, reminder_time) VALUES (%s, %s, %s, %s)",
                   (title, description, deadline, reminder_time))
    mysql.connection.commit()
    return jsonify({"message": "Task created successfully"}), 201
```

---

## **Frontend - User Interface**

The frontend is built with HTML, CSS, and JavaScript, and interacts with the Flask API to manage tasks.

- **Task List View**: Displays all tasks with their title, description, deadline, and reminder time.
- **Add Task Form**: A form to enter new tasks, including title, description, deadline, and reminder time.
- **Task Update**: Option to mark tasks as completed or update the task details.

Here’s an example of adding a new task using JavaScript with an AJAX request:

```javascript
fetch('http://localhost:5000/tasks', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: 'Study for Exam',
        description: 'Study the chapters of Math for the upcoming exam.',
        deadline: '2024-12-10T18:00',
        reminder_time: '2024-12-10T17:00'
    })
})
.then(response => response.json())
.then(data => alert(data.message))
.catch(error => console.error('Error:', error));
```

---

## **Reminder and Notification System**

This feature uses Python’s `schedule` library to check the database at regular intervals for tasks whose reminder time has come.

For email notifications, the Flask-Mail library can be used to send emails about upcoming deadlines. For sound alarms, the `playsound` library will trigger a notification sound.

### Example of using `schedule` to trigger reminders:

```python
import schedule
import time
from playsound import playsound

def check_reminders():
    # Check the database for tasks whose reminder time has come
    playsound('alarm_sound.mp3')

schedule.every(1).minute.do(check_reminders)
```

---

## **Running the Application**

To run the application:

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open the `index.html` file in a browser or use a local server.

3. The application should be accessible via `http://localhost:5000`.

---

## **Contributing**

If you’d like to contribute to this project, fork the repository, make your changes, and submit a pull request. Make sure to follow best coding practices and describe your changes in detail.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
