# College Scheduler Web Application

This is a **College Scheduler** web application designed to help students schedule their study sessions, internship preparations, exams, and other important tasks. The application provides functionalities such as creating, viewing, updating, and deleting schedules, along with setting alarms and notifications for reminders.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)
4. [Backend - Flask API](#backend-flask-api)
5. [Frontend - User Interface](#frontend-user-interface)
6. [Database Setup (MySQL)](#database-setup-mysql)
7. [Notification System](#notification-system)
8. [Running the Application](#running-the-application)
9. [Contributing](#contributing)
10. [License](#license)

---

## Project Overview

The **College Scheduler** web application is a tool for college students to manage their time effectively. It allows users to:

- Add study sessions, exam preparations, and other events.
- View and manage scheduled tasks.
- Set alarms and alerts for reminders of upcoming events.
- Delete tasks when they are no longer needed.

The application uses **Flask** for the backend, **MySQL** for database management, and a simple **HTML/CSS/JavaScript** frontend to interact with the user.

---

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Scheduler**: Python `schedule` library
- **Notification**: Playsound (for sound alarms)

---

## Setup and Installation

### Prerequisites

Before starting, ensure you have the following installed:

1. Python 3.x
2. MySQL Server
3. Flask
4. MySQL Connector for Python
5. JavaScript and browser for the frontend

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/college-scheduler.git
cd college-scheduler
```

### Step 2: Install Dependencies

To install the necessary Python dependencies, create a virtual environment and activate it.

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```

Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up MySQL Database

You need to set up MySQL for the project. Follow these steps:

1. Open MySQL Command Line or MySQL Workbench.
2. Create a new database for the project:

   ```sql
   CREATE DATABASE college_scheduler;
   ```

3. Run the SQL script to create necessary tables (Schedule Table) or use the following SQL:

   ```sql
   CREATE TABLE Schedules (
       schedule_id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT NOT NULL,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       start_time DATETIME NOT NULL,
       end_time DATETIME NOT NULL,
       alert_time DATETIME NOT NULL,
       FOREIGN KEY (user_id) REFERENCES Users(user_id)
   );
   ```

4. Configure your MySQL connection in `app.py`:

   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'your-password'
   app.config['MYSQL_DB'] = 'college_scheduler'
   ```

### Step 4: Frontend Setup

The frontend files are located in the `templates/` folder. You can open `index.html` directly in your browser or use a local server to run it.

---

## Backend - Flask API

The backend is built with Flask and is responsible for handling all the routes that deal with adding, retrieving, and deleting schedules. Here’s how the backend works:

### Routes:

- **GET /get_schedules/<user_id>**: Fetches all schedules for a given user.
- **POST /add_schedule**: Adds a new schedule to the database.
- **DELETE /delete_schedule/<schedule_id>**: Deletes a specific schedule.

Each route interacts with the MySQL database to retrieve or store data.

Example of adding a schedule via POST request:

```python
@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    data = request.get_json()
    title = data['title']
    description = data['description']
    start_time = data['start_time']
    end_time = data['end_time']
    alert_time = data['alert_time']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO Schedules (title, description, start_time, end_time, alert_time) VALUES (%s, %s, %s, %s, %s)",
                   (title, description, start_time, end_time, alert_time))
    mysql.connection.commit()
    return jsonify({"message": "Schedule added successfully"}), 200
```

---

## Frontend - User Interface

The frontend is designed with HTML, CSS, and JavaScript. The user interface allows students to:

1. **Add Schedules**: Users can input title, description, start time, end time, and alert time to create a new schedule.
2. **View Schedules**: The schedules are displayed in a table format.
3. **Delete Schedules**: Users can delete a schedule by clicking the "Delete" button next to each schedule.

AJAX is used for sending and receiving data from the Flask API without reloading the page.

Example of sending a POST request to add a schedule:

```javascript
fetch('http://localhost:5000/add_schedule', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: 'Exam Preparation',
        description: 'Prepare for exam tomorrow',
        start_time: '2024-12-01T08:00',
        end_time: '2024-12-01T12:00',
        alert_time: '2024-12-01T07:30'
    })
})
.then(response => response.json())
.then(data => alert(data.message))
.catch(error => console.error('Error:', error));
```

---

## Database Setup (MySQL)

To ensure your application works smoothly, ensure that your **MySQL database** is properly set up as outlined in the **Setup and Installation** section. 

- Create a `college_scheduler` database.
- Create tables for storing user schedules.
- Ensure your Flask app is correctly connected to MySQL using the correct credentials.

---

## Notification System

The application includes an alarm/notification system that uses the Python **schedule** library. The `notification.py` script checks the database every minute to trigger alarms for schedules with upcoming alert times.

When a schedule's alert time is reached, the system plays a sound alarm and removes or marks the schedule as alerted in the database.

### Example:

```python
import schedule
import time
from playsound import playsound

def check_alerts():
    # Check the database for schedules with alert times
    # Trigger alarms using playsound
    playsound('alarm_sound.mp3')

schedule.every(1).minute.do(check_alerts)
```

---

## Running the Application

To run the application:

1. Ensure the Flask backend is running:

   ```bash
   python app.py
   ```

2. Open the `index.html` file in a browser, or use a local server to serve the HTML.

3. The application should be accessible via `http://localhost:5000`.

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Please make sure to follow best practices for coding standards and provide a detailed description of your changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
