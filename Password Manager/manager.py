import getpass
from encryption import hash_password, verify_password, encrypt_password, decrypt_password
from db_handler import initialize_database, add_credential, retrieve_credential, delete_credential

# Initialize the database and prompt for a master password on first use
MASTER_PASSWORD_HASH = None

def set_master_password():
    """Sets the master password by hashing it and storing it in a local file."""
    global MASTER_PASSWORD_HASH
    master_password = getpass.getpass("Set a master password: ")
    confirm_password = getpass.getpass("Confirm master password: ")

    if master_password == confirm_password:
        MASTER_PASSWORD_HASH = hash_password(master_password)
        with open("master_password.txt", "w") as f:
            f.write(MASTER_PASSWORD_HASH)
        print("Master password set successfully!")
    else:
        print("Passwords do not match. Please try again.")
        set_master_password()

def load_master_password():
    """Loads the hashed master password from file."""
    global MASTER_PASSWORD_HASH
    try:
        with open("master_password.txt", "r") as f:
            MASTER_PASSWORD_HASH = f.read().strip()
    except FileNotFoundError:
        print("No master password found. Setting a new one...")
        set_master_password()

def verify_master_password():
    """Prompts for the master password and verifies it against the hash."""
    master_password = getpass.getpass("Enter master password: ")
    if verify_password(MASTER_PASSWORD_HASH, master_password):
        print("Access granted.")
        return True
    else:
        print("Incorrect password.")
        return False

def main_menu():
    """Displays the main menu and handles user choices."""
    print("\n--- Secure Password Manager ---")
    print("1. Add new credential")
    print("2. View credential")
    print("3. Delete credential")
    print("4. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        add_new_credential()
    elif choice == "2":
        view_credential()
    elif choice == "3":
        delete_credential_option()
    elif choice == "4":
        print("Exiting the Password Manager. Goodbye!")
        exit()
    else:
        print("Invalid option. Please select again.")
        main_menu()

def add_new_credential():
    """Prompts the user for a new credential and stores it securely."""
    service_name = input("Enter service name: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    encrypted_password = encrypt_password(password)
    add_credential(service_name, username, encrypted_password)
    print(f"Credential for {service_name} added successfully.")

def view_credential():
    """Prompts the user for a service name and retrieves the stored credential."""
    service_name = input("Enter service name to retrieve: ")
    credential = retrieve_credential(service_name)
    if credential:
        print(f"Username: {credential['username']}")
        print(f"Password: {decrypt_password(credential['password'])}")
    else:
        print("No credential found for that service.")

def delete_credential_option():
    """Prompts the user for a service name and deletes the credential."""
    service_name = input("Enter service name to delete: ")
    delete_credential(service_name)

if __name__ == "__main__":
    initialize_database()
    load_master_password()
    
    if verify_master_password():
        while True:
            main_menu()

