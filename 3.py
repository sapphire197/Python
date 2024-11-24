#notification.py

#pip install schedule

import time
import schedule
from datetime import datetime
from playsound import playsound  # To play an alert sound when time arrives

# Function to check if the alert time is reached
def check_alerts():
    # Here you will fetch the schedules with alerts from the database
    from app import mysql  # Importing the Flask app to access the database
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Schedules WHERE alert_time <= NOW() AND alert_time > DATE_SUB(NOW(), INTERVAL 1 MINUTE)")
    schedules = cursor.fetchall()

    for schedule in schedules:
        alert_time = schedule['alert_time']
        title = schedule['title']
        
        # Trigger the alarm
        print(f"ALERT: {title} is scheduled at {alert_time}")
        playsound('alarm_sound.mp3')  # Play sound (you can add any mp3 sound file)

        # You can also send a notification here (email, SMS, etc.)

        # After the alert, delete or mark the schedule as alerted (optional)
        cursor.execute("DELETE FROM Schedules WHERE schedule_id = %s", (schedule['schedule_id'],))
        mysql.connection.commit()

# Function to schedule the check every minute
def run_alarm():
    schedule.every(1).minute.do(check_alerts)  # Run check every minute
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_alarm()
