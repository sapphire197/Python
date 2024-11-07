import mysql.connector
from mysql.connector import Error
from encryption import encrypt, decrypt, derive_key

# MySQL connection details - update these with your MySQL credentials
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database"

def create_connection():
    """Creates and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    """Initializes the database and creates the credentials table if it doesn't exist."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS credentials (
                    service VARCHAR(255) PRIMARY KEY,
                    username VARCHAR(255),
                    password TEXT
                )
            ''')
            connection.commit()
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            cursor.close()
            connection.close()

def add_credential(service: str, username: str, password: str):
    """Adds an encrypted credential to the database."""
    key = derive_key("master_password")  # Replace "master_password" with actual master password
    encrypted_password = encrypt(password, key)
    
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO credentials (service, username, password)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE username=%s, password=%s
            ''', (service, username, encrypted_password, username, encrypted_password))
            connection.commit()
        except Error as e:
            print(f"Error adding credential: {e}")
        finally:
            cursor.close()
            connection.close()

def retrieve_credential(service: str):
    """Retrieves and decrypts a credential from the database."""
    key = derive_key("master_password")  # Replace "master_password" with actual master password
    
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT username, password FROM credentials WHERE service = %s', (service,))
            row = cursor.fetchone()
            
            if row:
                username, encrypted_password = row
                password = decrypt(encrypted_password, key)
                return {'username': username, 'password': password}
            return None
        except Error as e:
            print(f"Error retrieving credential: {e}")
        finally:
            cursor.close()
            connection.close()

def delete_credential(service: str):
    """Deletes a credential from the database."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM credentials WHERE service = %s', (service,))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting credential: {e}")
        finally:
            cursor.close()
            connection.close()

# Initialize the database when the module is imported
init_db()
