-- Create a database
CREATE DATABASE CollegeScheduler;

-- Use the database
USE CollegeScheduler;

-- Create a table for users
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255)
);

-- Create a table for schedules
CREATE TABLE Schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    description TEXT,
    start_time DATETIME,
    end_time DATETIME,
    alert_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Insert sample data (optional)
INSERT INTO Users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password123');
INSERT INTO Schedules (user_id, title, description, start_time, end_time, alert_time) 
VALUES (1, 'Math Prep', 'Prepare for math exam', '2024-11-25 09:00:00', '2024-11-25 11:00:00', '2024-11-25 08:50:00');
