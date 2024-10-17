def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    entry = input("Write your diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(f"{date}: {entry}\n")
    print("Entry added successfully!")

def view_entries():
    print("\n--- Your Diary ---")
    with open("diary.txt", "r") as file:
        entries = file.readlines()
        for entry in entries:
            print(entry.strip())

def main():
    while True:
        print("\n--- Personal Diary ---")
        print("1. Add Diary Entry")
        print("2. View Diary Entries")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
