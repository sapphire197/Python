# database.py
import sqlite3

def connect_db():
    """Connect to SQLite database or create it if not exists."""
    connection = sqlite3.connect("academic_tracker.db")
    cursor = connection.cursor()

    # Create Subjects table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        credit_hours INTEGER NOT NULL
    )
    ''')

    # Create Grades table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL,
        grade TEXT NOT NULL,
        semester TEXT NOT NULL,
        FOREIGN KEY (subject_id) REFERENCES Subjects(id)
    )
    ''')

    connection.commit()
    connection.close()

def add_subject(subject_name, credit_hours):
    """Add a new subject to the database."""
    connection = sqlite3.connect("academic_tracker.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Subjects (subject_name, credit_hours) VALUES (?, ?)", 
                   (subject_name, credit_hours))
    connection.commit()
    connection.close()

def fetch_subjects():
    """Fetch all subjects from the database."""
    connection = sqlite3.connect("academic_tracker.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Subjects")
    subjects = cursor.fetchall()
    connection.close()
    return subjects

def add_grade(subject_id, grade, semester):
    """Add a grade for a subject in a specific semester."""
    connection = sqlite3.connect("academic_tracker.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Grades (subject_id, grade, semester) VALUES (?, ?, ?)", 
                   (subject_id, grade, semester))
    connection.commit()
    connection.close()

def fetch_grades():
    """Fetch all grades from the database."""
    connection = sqlite3.connect("academic_tracker.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Grades")
    grades = cursor.fetchall()
    connection.close()
    return grades

# Initialize the database
if __name__ == "__main__":
    connect_db()
    print("Database setup complete.")
