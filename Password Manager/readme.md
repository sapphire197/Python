## Secure Password Manager

### Description

The **Secure Password Manager** is a Python-based application for securely storing, retrieving, and managing credentials for various services. It uses AES-GCM encryption to store passwords securely in a MySQL database, accessed through MySQL Workbench. This project serves as a robust solution for managing credentials with encryption, safe password hashing, and database integration.

### Features

- **AES-GCM Encryption** for strong password security
- **MySQL Database Integration** via MySQL Workbench
- **Credential Management**: Add, retrieve, and delete encrypted credentials for any service
- **Master Password Protection**: Safeguard access with a hashed master password

---

### Prerequisites

1. **Python 3.8 or higher**
2. **MySQL** installed and accessible via **MySQL Workbench**
3. **MySQL Credentials** with a database set up for this application (e.g., `password_manager_db`)

### Libraries Required

Install the following Python packages by running the command:
```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
pycryptodome==3.15.0            # For AES encryption and decryption
mysql-connector-python==8.0.33  # For MySQL database connectivity
```

---

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/secure-password-manager.git
   cd secure-password-manager
   ```

2. **Configure MySQL Database**:
   - Open MySQL Workbench, create a new database for the project (e.g., `password_manager_db`), and note the credentials.

   - Run the following SQL command in MySQL Workbench:
     ```sql
     CREATE DATABASE password_manager_db;
     ```

3. **Configure Database Connection**:
   - Update `db_handler.py` with your MySQL database credentials:
     ```python
     DB_HOST = "localhost"           # MySQL host (often 'localhost')
     DB_USER = "your_username"       # MySQL username
     DB_PASSWORD = "your_password"   # MySQL password
     DB_NAME = "password_manager_db" # Name of the database created
     ```

4. **Initialize the Database**:
   - The table for storing credentials will be created automatically when you run the application.

5. **Set Up Master Password**:
   - Run the application, select the option to create a master password, and follow prompts to set a secure password. This hashed password will be used to verify access each time.

---

### Usage

Run the application and follow these steps:

1. **Start the Application**:
   ```bash
   python manager.py
   ```

2. **Main Menu**:
   - **Option 1**: Add New Credential – Stores an encrypted username and password for a given service.
   - **Option 2**: View Credential – Retrieves and decrypts the credentials for a specified service.
   - **Option 3**: Delete Credential – Deletes the credentials for a specified service.
   - **Option 4**: Exit – Closes the application.

3. **Adding a Credential**:
   - Select **Option 1**.
   - Enter the service name, username, and password when prompted. The data will be encrypted and stored in the database.
   
4. **Viewing a Credential**:
   - Select **Option 2**.
   - Enter the service name for which you wish to retrieve credentials. If found, the username and decrypted password will be displayed.

5. **Deleting a Credential**:
   - Select **Option 3**.
   - Enter the service name to remove credentials for that service from the database.

---

### Project Structure

The project consists of the following modules:

1. **`encryption.py`**:
   - Handles all encryption, decryption, and hashing functionalities.
   - Uses AES-GCM encryption to securely store and retrieve passwords.
   - Provides password hashing for master password verification.

2. **`db_handler.py`**:
   - Contains functions for connecting to the MySQL database, creating tables, adding, retrieving, and deleting credentials.
   - Initializes the database with a `credentials` table if it doesn't already exist.
   - Handles secure, encrypted storage of passwords.

3. **`manager.py`**:
   - Provides the command-line interface for user interaction.
   - Manages the main menu, where users can choose to add, view, or delete credentials.
   - Utilizes the `getpass` function to securely prompt for passwords.

---

### Example Workflow

1. **Add a Credential**:
   - Run the application with `python manager.py`.
   - Select **1** for "Add new credential".
   - Enter:
     ```
     Service Name: github
     Username: your_username
     Password: your_password
     ```
   - The service, username, and encrypted password will be added to the database.

2. **View a Credential**:
   - Run the application with `python manager.py`.
   - Select **2** for "View credential".
   - Enter:
     ```
     Service Name: github
     ```
   - The stored username and decrypted password will be displayed if the service exists.

3. **Delete a Credential**:
   - Run the application with `python manager.py`.
   - Select **3** for "Delete credential".
   - Enter:
     ```
     Service Name: github
     ```
   - The credential for "github" will be deleted if it exists.

---

### Security Insights

- **Encryption**: The application uses **AES-GCM**, a modern encryption standard for secure data encryption. The encryption process combines a randomly generated nonce with the encryption key, producing ciphertext and an authentication tag for integrity verification.

- **Password Hashing**: The master password is hashed using `scrypt`, a secure key derivation function, making it difficult to recover the password even if the hash is compromised.

- **Database Security**: All sensitive information is stored in an encrypted format in MySQL, so even if the database is accessed by an unauthorized user, the data remains secure.

### Future Enhancements

- **Password Strength Checker**: Integrate a feature to assess the strength of passwords before storing them.
- **Two-Factor Authentication**: Add support for two-factor authentication to increase security.
- **User Interface**: Develop a graphical user interface (GUI) using a library like Tkinter for a more user-friendly experience.

---

### Troubleshooting

- **Database Connection Error**: Ensure that MySQL Workbench is properly configured and the provided credentials are correct.
- **Encryption Errors**: If encountering issues with encryption, confirm that `pycryptodome` is installed and compatible with your Python version.

### Acknowledgments

This project is built with Python, leveraging AES encryption and MySQL for secure credential management.
