# Secure Password Manager

## Overview
The **Secure Password Manager** is a Python-based application that helps users safely store, retrieve, and manage their passwords with robust encryption. This manager uses **AES encryption** to protect your passwords, with access controlled by a **Master Password**. The project also includes additional features like a password generator and strength checker to help create secure credentials.

---

## Features
- **Master Password Protection**: Authenticates access to stored credentials with a master password, hashed and stored securely.
- **Add New Credentials**: Encrypts and securely stores new login credentials.
- **Retrieve Credentials**: Decrypts and retrieves stored credentials for easy access.
- **Delete Credentials**: Enables users to delete specific credentials.
- **Auto-Password Generator**: Creates strong random passwords with customizable options.
- **Password Strength Checker**: Rates password strength based on length and complexity.
- **Encrypted Storage**: Uses AES encryption to keep passwords secure.
- **Data Backup & Export**: Option to export encrypted passwords to a secure backup file.

---

## Project Structure

```
password_manager/
├── manager.py              # Main script to run the password manager
├── encryption.py           # Module for encryption and decryption
├── db_handler.py           # Manages database operations (CRUD)
├── password_generator.py    # Generates secure passwords
├── checker.py              # Password strength checker
├── requirements.txt        # List of dependencies
├── README.md               # Project overview and instructions
└── .gitignore              # Specifies files to ignore in Git
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   ```
2. **Install Required Packages**:
   Ensure you have Python installed. Then, install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Password Manager**:
   ```bash
   python manager.py
   ```

---

## Usage

1. **Launch the Manager**: 
   - When you first run the program, set up your **Master Password** (remember to keep this safe, as it can’t be recovered).

2. **Main Menu Options**:
   - **Add Credentials**: Enter details (website/app, username, password). You can also use the built-in password generator.
   - **Retrieve Credentials**: Provide the service name to retrieve decrypted credentials.
   - **Delete Credentials**: Specify the service name to delete the credentials.

3. **Password Generator**:
   - Use the generator to create strong passwords, with options for length, special characters, numbers, and uppercase letters.

4. **Backup and Restore**:
   - Backup encrypted credentials and restore them when needed.

---

## Security Information
- **Encryption**: Uses **AES-256** to encrypt and store passwords securely.
- **Master Password**: Secured by **SHA-256 hashing** for safe storage and authentication.
- **Data Protection**: Credentials are encrypted in storage and only decrypted during retrieval.
- **Note**: Remember the Master Password, as it is crucial for access and cannot be recovered.

---

## Example Code Snippets

Here’s a quick example of how to add and retrieve a password:

```python
# Adding a credential
from db_handler import add_credential
add_credential("example.com", "username", "password")

# Retrieving a credential
from db_handler import retrieve_credential
print(retrieve_credential("example.com"))
```

---

## Dependencies
This project uses the following packages:
- `pycryptodome`: For AES encryption.
- `sqlite3`: For storing encrypted credentials.
  
To install all dependencies, use:
```bash
pip install -r requirements.txt
```

---

## Future Enhancements
1. **Two-Factor Authentication**: Add a second layer of security.
2. **Graphical User Interface (GUI)**: Make the password manager user-friendly.
3. **Password Expiry Notification**: Remind users to update old passwords.

---

## Contributing
1. **Fork the Repository**
2. **Create a Branch** for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit Changes** with descriptive messages:
   ```bash
   git commit -m "Add feature"
   ```
4. **Push Changes**:
   ```bash
   git push origin feature-name
   ```
5. **Create a Pull Request** on GitHub

