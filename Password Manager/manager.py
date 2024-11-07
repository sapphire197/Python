from db_handler import add_credential, retrieve_credential, delete_credential
from encryption import hash_master_password, verify_master_password
from getpass import getpass

def create_master_password():
    """Sets up the master password."""
    master_password = getpass("Set your master password: ")
    hashed_password = hash_master_password(master_password)
    # Save hashed_password securely (e.g., in a config file or encrypted storage)
    print("Master password set and saved.")

def add_service():
    """Adds a new service with username and password."""
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = getpass("Enter the password: ")
    add_credential(service, username, password)
    print("Credential added successfully.")

def view_service():
    """Retrieves and displays credentials for a service."""
    service = input("Enter the service name: ")
    credentials = retrieve_credential(service)
    if credentials:
        print(f"Username: {credentials['username']}")
        print(f"Password: {credentials['password']}")
    else:
        print("No credentials found for the specified service.")

def delete_service():
    """Deletes a service's credentials."""
    service = input("Enter the service name to delete: ")
    success = delete_credential(service)
    if success:
        print("Credential deleted successfully.")
    else:
        print("No credential found for the specified service.")

def main():
    """Main menu for the password manager."""
    print("Welcome to the Password Manager")
    while True:
        print("\nOptions:")
        print("1. Add new credential")
        print("2. View credential")
        print("3. Delete credential")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_service()
        elif choice == '2':
            view_service()
        elif choice == '3':
            delete_service()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
