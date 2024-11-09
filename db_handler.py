import mysql.connector

DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "smart_notes_db"

def create_connection():
    """Establish a connection to the MySQL database."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

def initialize_db():
    """Initialize the database with required tables."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS smart_notes_db")
    cursor.execute("USE smart_notes_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            content TEXT,
            category VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_note(title, content, category):
    """Add a new note to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content, category) VALUES (%s, %s, %s)",
                   (title, content, category))
    conn.commit()
    conn.close()

def get_all_notes():
    """Retrieve all notes from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return notes

def search_notes(keyword):
    """Search for notes based on a keyword."""
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM notes WHERE title LIKE %s OR content LIKE %s"
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    conn.close()
    return results

def delete_note(note_id):
    """Delete a note by its ID."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    conn.close()
