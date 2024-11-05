import sqlite3
from encryption import encrypt, decrypt, derive_key

DATABASE_FILE = "password_manager.db"

def init_db():
    """Initializes the database and creates the credentials table if it doesn't exist."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS credentials (
                service TEXT PRIMARY KEY,
                username TEXT,
                password TEXT
            )
        ''')
        conn.commit()

def add_credential(service: str, username: str, password: str):
    """Adds an encrypted credential to the database."""
    key = derive_key("master_password")  # Replace "master_password" with actual master password
    encrypted_password = encrypt(password, key)
    
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO credentials (service, username, password)
            VALUES (?, ?, ?)
        ''', (service, username, encrypted_password))
        conn.commit()

def retrieve_credential(service: str):
    """Retrieves and decrypts a credential from the database."""
    key = derive_key("master_password")  # Replace "master_password" with actual master password
    
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, password FROM credentials WHERE service = ?', (service,))
        row = cursor.fetchone()
        
        if row:
            username, encrypted_password = row
            password = decrypt(encrypted_password, key)
            return {'username': username, 'password': password}
        return None

def delete_credential(service: str):
    """Deletes a credential from the database."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM credentials WHERE service = ?', (service,))
        conn.commit()
        return cursor.rowcount > 0

# Initialize the database when the module is imported
init_db()
