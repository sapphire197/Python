import mysql.connector
from encryption import encrypt_content, decrypt_content

DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "smart_notes_db"

def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            content TEXT,
            category VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_note(title, content, category):
    conn = connect_db()
    cursor = conn.cursor()
    encrypted_content = encrypt_content(content)
    cursor.execute("INSERT INTO notes (title, content, category) VALUES (%s, %s, %s)", (title, encrypted_content, category))
    conn.commit()
    conn.close()

def get_all_notes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    results = cursor.fetchall()
    conn.close()
    return [(note[0], note[1], decrypt_content(note[2]), note[3], note[4]) for note in results]

def delete_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    conn.close()
