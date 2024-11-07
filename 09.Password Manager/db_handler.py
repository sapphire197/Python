import mysql.connector
from mysql.connector import Error

# MySQL database configuration
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "password_manager_db"

def create_connection():
    """Establish a database connection."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print("Connection to MySQL database successful.")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def initialize_database():
    """Creates the credentials table if it does not already exist."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS credentials (
            id INT AUTO_INCREMENT PRIMARY KEY,
            service_name VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password TEXT NOT NULL
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()

def add_credential(service_name, username, encrypted_password):
    """Inserts a new credential into the credentials table."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO credentials (service_name, username, password)
        VALUES (%s, %s, %s);
        """
        cursor.execute(insert_query, (service_name, username, encrypted_password))
        connection.commit()
        cursor.close()
        connection.close()
        print("Credential added successfully.")

def retrieve_credential(service_name):
    """Fetches the credential for a given service name."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        select_query = "SELECT username, password FROM credentials WHERE service_name = %s;"
        cursor.execute(select_query, (service_name,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return {"username": result[0], "password": result[1]}
        else:
            print("No credential found for the specified service.")
            return None

def delete_credential(service_name):
    """Deletes the credential for a specified service name."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        delete_query = "DELETE FROM credentials WHERE service_name = %s;"
        cursor.execute(delete_query, (service_name,))
        connection.commit()
        cursor.close()
        connection.close()
        print("Credential deleted successfully.")
