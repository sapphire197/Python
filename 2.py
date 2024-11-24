#app.py

#pip install flask flask-mysql flask-cors


from flask import Flask, request, jsonify
from flask_mysql_connector import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DATABASE'] = 'CollegeScheduler'

mysql = MySQL(app)

@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    data = request.json
    query = """
        INSERT INTO Schedules (user_id, title, description, start_time, end_time, alert_time)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        data['user_id'], data['title'], data['description'],
        data['start_time'], data['end_time'], data['alert_time']
    )
    cursor = mysql.connection.cursor()
    cursor.execute(query, values)
    mysql.connection.commit()
    return jsonify({'message': 'Schedule added successfully'})

@app.route('/get_schedules/<int:user_id>', methods=['GET'])
def get_schedules(user_id):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Schedules WHERE user_id = %s", (user_id,))
    schedules = cursor.fetchall()
    return jsonify(schedules)

@app.route('/delete_schedule/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM Schedules WHERE schedule_id = %s", (schedule_id,))
    mysql.connection.commit()
    return jsonify({'message': 'Schedule deleted successfully'})

@app.route('/update_schedule/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    data = request.json
    query = """
        UPDATE Schedules 
        SET title = %s, description = %s, start_time = %s, end_time = %s, alert_time = %s
        WHERE schedule_id = %s
    """
    values = (
        data['title'], data['description'], data['start_time'], 
        data['end_time'], data['alert_time'], schedule_id
    )
    cursor = mysql.connection.cursor()
    cursor.execute(query, values)
    mysql.connection.commit()
    return jsonify({'message': 'Schedule updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
