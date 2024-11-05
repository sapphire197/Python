from getpass import getpass
from encryption import hash_master_password, verify_master_password
from db_handler import add_credential, retrieve_credential, delete_credential
from password_generator import generate_password
from checker import check_password_strength

def authenticate_master_password():
    try:
        # Ask user for master password
        master_password = getpass("Enter your master password: ")
        # Verify the master password
        if not verify_master_password(master_password):
            print("Incorrect master password. Access denied.")
            return False
        return True
    except Exception as e:
        print(f"Authentication failed: {e}")
        return False

def main_menu():
    while True:
        print("\nPassword Manager")
        print("1. Add New Credential")
        print("2. Retrieve Credential")
        print("3. Delete Credential")
        print("4. Generate Strong Password")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = getpass("Enter password (leave blank to auto-generate): ")
            
            if not password:
                password = generate_password()
                print(f"Generated Password: {password}")
            
            if check_password_strength(password) < 3:
                print("Warning: Password is weak.")
            
            add_credential(service, username, password)
            print("Credential added successfully.")
        
        elif choice == "2":
            service = input("Enter service name to retrieve: ")
            credential = retrieve_credential(service)
            if credential:
                print(f"Username: {credential['username']}\nPassword: {credential['password']}")
            else:
                print("Credential not found.")
        
        elif choice == "3":
            service = input("Enter service name to delete: ")
            if delete_credential(service):
                print("Credential deleted successfully.")
            else:
                print("Credential not found.")
        
        elif choice == "4":
            length = int(input("Enter desired password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        
        elif choice == "5":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("Welcome to Secure Password Manager")
    if authenticate_master_password():
        main_menu()
