# app.py

# app.py
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import schedule
import time
from playsound import playsound
from datetime import datetime
from threading import Thread

# Initialize Flask app and MySQL
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your-password'
app.config['MYSQL_DB'] = 'task_manager'

mysql = MySQL(app)

# Task Model
class Task:
    def __init__(self, task_id, title, description, deadline, reminder_time, status='pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.reminder_time = reminder_time
        self.status = status

# Home Route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Task Management System!"})

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    task_list = []
    for task in tasks:
        task_list.append({
            "task_id": task[0],
            "title": task[1],
            "description": task[2],
            "deadline": task[3],
            "reminder_time": task[4],
            "status": task[5]
        })
    return jsonify(task_list)

# Route to create a task
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

# Route to update a task
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data['title']
    description = data['description']
    deadline = data['deadline']
    reminder_time = data['reminder_time']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tasks SET title = %s, description = %s, deadline = %s, reminder_time = %s WHERE task_id = %s",
                   (title, description, deadline, reminder_time, task_id))
    mysql.connection.commit()
    return jsonify({"message": "Task updated successfully"}), 200

# Route to delete a task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE task_id = %s", [task_id])
    mysql.connection.commit()
    return jsonify({"message": "Task deleted successfully"}), 200

# Reminder function to check tasks and play sound when reminder time is reached
def check_reminders():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE reminder_time <= %s AND status = 'pending'", [datetime.now()])
    tasks = cursor.fetchall()

    for task in tasks:
        print(f"Reminder: Task '{task[1]}' is due!")
        playsound('alarm_sound.mp3')

# Schedule reminder checks every minute
def schedule_reminder_checks():
    schedule.every(1).minute.do(check_reminders)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Start reminder checking in a separate thread
if __name__ == '__main__':
    reminder_thread = Thread(target=schedule_reminder_checks)
    reminder_thread.daemon = True
    reminder_thread.start()
    app.run(debug=True)
