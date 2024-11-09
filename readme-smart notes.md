# Smart Notes Organizer with GUI

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
   - [Required Python Libraries](#required-python-libraries)
5. [Setup Instructions](#setup-instructions)
   - [Step 1: Generate the Encryption Key](#1-generate-the-encryption-key)
   - [Step 2: Set Up the MySQL Database](#2-set-up-the-mysql-database)
   - [Step 3: Run the Application](#3-run-the-application)
6. [Detailed File Explanations](#detailed-file-explanations)
   - [encryption.py](#1-encryptionpy)
   - [db_handler.py](#2-db_handlerpy)
   - [ui.py](#3-uipy)
7. [How to Use the Application](#how-to-use-the-application)
   - [Adding a Note](#adding-a-note)
   - [Viewing Notes](#viewing-notes)
   - [Deleting a Note](#deleting-a-note)
8. [Screenshots (Sample GUI)](#screenshots-sample-gui)
9. [Potential Enhancements](#potential-enhancements)
10. [Troubleshooting](#troubleshooting)
    - [MySQL Connection Error](#1-mysql-connection-error)
    - [Encryption Key Issues](#2-encryption-key-issues)
    - [GUI Issues](#3-gui-issues)
11. [Technologies Used](#technologies-used)
12. [Contributing](#contributing)

---

## Project Overview
The **Smart Notes Organizer** is a secure and efficient application designed to help users manage their notes. Built with **Tkinter**, the app uses **encryption** to protect sensitive information and stores data securely in a **MySQL database**. It allows users to create, view, and delete categorized notes while ensuring data privacy through encryption.

---

## Features
1. **Graphical User Interface (GUI)**:
   - Simple and user-friendly interface.
   - Built using Python’s `tkinter` library.

2. **Encryption**:
   - Uses `cryptography` for encrypting and decrypting note contents.
   - Ensures data privacy by encrypting notes before storing.

3. **MySQL Database Integration**:
   - Stores encrypted notes, titles, categories, and timestamps.
   - Secure data management with MySQL.

4. **Categorization and Organization**:
   - Categorize notes for better organization.
   - Easily manage and navigate through notes.

---

## Project Structure
```
Smart Notes Organizer
│
├── encryption.py         # Handles encryption and decryption
├── db_handler.py         # Manages MySQL database interactions
├── note_manager.py       # Functions to manage notes
├── ui.py                 # GUI implementation using Tkinter
├── requirements.txt      # Python dependencies
└── secret.key            # Secret key for encryption (generated)
```

---

## Prerequisites
Ensure you have the following software installed:
- Python 3.x
- MySQL Server
- `pip` for managing Python packages

### Required Python Libraries
Install dependencies using:
```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```
mysql-connector-python==8.0.33
cryptography==41.0.1
tkinter (usually pre-installed with Python)
```

---

## Setup Instructions

### 1. Generate the Encryption Key
Generate the encryption key using:
```bash
python encryption.py
```
This creates a `secret.key` file used for encrypting and decrypting data.

### 2. Set Up the MySQL Database
Create a MySQL database named `smart_notes_db` and update credentials in `db_handler.py`:
```python
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "smart_notes_db"
```

Initialize the database tables:
```bash
python -c "from db_handler import initialize_db; initialize_db()"
```

### 3. Run the Application
Start the GUI by running:
```bash
python ui.py
```

---

## Detailed File Explanations

### 1. `encryption.py`
Handles encryption and decryption using the `cryptography.fernet` library.

- **Functions**:
  - `generate_key()`: Generates a unique encryption key.
  - `load_key()`: Loads the encryption key.
  - `encrypt_content(content)`: Encrypts note content.
  - `decrypt_content(encrypted_content)`: Decrypts content.

### 2. `db_handler.py`
Handles database operations, including adding, retrieving, and deleting notes.

- **Functions**:
  - `connect_db()`: Connects to the MySQL database.
  - `initialize_db()`: Creates the `notes` table.
  - `add_note()`: Adds a new encrypted note.
  - `get_all_notes()`: Retrieves and decrypts notes.
  - `delete_note()`: Deletes a selected note.

### 3. `ui.py`
Provides a graphical user interface using `tkinter`.

- **Features**:
  - Add, view, and delete notes.
  - Dynamic note listing with refresh functionality.
  - Secure data handling with encryption.

---

## How to Use the Application

### Adding a Note
1. Enter the **Title**, **Content**, and **Category**.
2. Click the **"Add Note"** button.
3. The note is securely encrypted and saved.

### Viewing Notes
- View all notes in the listbox with their titles and categories.
- Decrypted content is displayed when selected.

### Deleting a Note
1. Select a note from the list.
2. Click the **"Delete Selected Note"** button to remove it.

---

## Screenshots (Sample GUI)
### Home Screen
A simple interface with options to manage notes.

### Adding a New Note
![Add Note Screen](example_add_note.png)

### Viewing All Notes
![View Notes Screen](example_view_notes.png)

---

## Potential Enhancements
- **Search Functionality**: Add search by title or category.
- **Edit Notes**: Implement functionality to update notes.
- **User Authentication**: Add password protection.
- **Cloud Integration**: Enable cloud backups for notes.

---

## Troubleshooting

### 1. MySQL Connection Error
Ensure your MySQL service is running and credentials are correct.

### 2. Encryption Key Issues
If the decryption fails, regenerate the key:
```bash
python encryption.py
```
Note: Regenerating the key will make existing encrypted notes unreadable.

### 3. GUI Issues
Ensure `tkinter` is installed (comes pre-installed with Python).

---

## Technologies Used
- **Python**: Core language for the project.
- **Tkinter**: Used for GUI development.
- **Cryptography**: For secure data encryption.
- **MySQL**: Database for storing notes.

---

## Contributing
Feel free to contribute by opening an issue or submitting a pull request. All contributions are welcome!

