import csv

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    description = input("Enter a short description: ")

    expenses.append([date, category, amount, description])
    with open("expenses.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

def view_expenses():
    print("\nDate       | Category     | Amount  | Description")
    print("-----------------------------------------------")
    with open("expenses.csv", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
