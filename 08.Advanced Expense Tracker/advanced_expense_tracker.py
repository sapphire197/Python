import tkinter as tk
from tkinter import messagebox, ttk
import json
from datetime import datetime
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# Path to save expense data
DATA_FILE = 'advanced_expense_data.json'

# Load expenses from JSON file
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = {"budget": 0, "expenses": []}
    return expenses

# Save expenses to JSON file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Set monthly budget
def set_budget():
    budget = budget_entry.get()
    if budget.isdigit():
        data = load_expenses()
        data["budget"] = int(budget)
        save_expenses(data)
        messagebox.showinfo("Success", "Monthly budget set!")
    else:
        messagebox.showerror("Error", "Please enter a valid number.")

# Add new expense
def add_expense():
    amount = amount_entry.get()
    description = description_entry.get()
    category = category_combobox.get()
    date = datetime.now().strftime("%Y-%m-%d")

    if amount.isdigit() and description and category:
        data = load_expenses()
        data["expenses"].append({
            "amount": int(amount),
            "description": description,
            "category": category,
            "date": date
        })
        save_expenses(data)
        check_budget(data)
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        category_combobox.set('')
        messagebox.showinfo("Success", "Expense added!")
    else:
        messagebox.showerror("Error", "Please enter all data fields.")

# Check if expenses exceed the budget
def check_budget(data):
    total_expenses = sum(item['amount'] for item in data['expenses'])
    if total_expenses > data["budget"]:
        messagebox.showwarning("Alert", "You have exceeded your monthly budget!")

# Display pie chart of expenses by category
def show_category_distribution():
    data = load_expenses()
    if not data["expenses"]:
        messagebox.showinfo("Info", "No expenses to display.")
        return

    categories = defaultdict(int)
    for expense in data["expenses"]:
        categories[expense["category"]] += expense["amount"]

    labels = list(categories.keys())
    sizes = list(categories.values())

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.show()

# Display monthly summary report
def monthly_summary():
    data = load_expenses()
    if not data["expenses"]:
        messagebox.showinfo("Info", "No expenses to display.")
        return

    total_expenses = sum(item['amount'] for item in data["expenses"])
    budget = data["budget"]
    summary_text = f"Total Expenses: {total_expenses}\nBudget: {budget}\nRemaining: {budget - total_expenses}"
    messagebox.showinfo("Monthly Summary", summary_text)

# Export expenses to CSV
def export_to_csv():
    data = load_expenses()
    filename = f"expense_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Category", "Amount"])
        for expense in data["expenses"]:
            writer.writerow([expense["date"], expense["description"], expense["category"], expense["amount"]])
    messagebox.showinfo("Exported", f"Expenses exported to {filename}")

# GUI setup
root = tk.Tk()
root.title("Advanced Expense Tracker")

# Budget UI Elements
tk.Label(root, text="Set Monthly Budget:").pack(pady=5)
budget_entry = tk.Entry(root, width=20)
budget_entry.pack()
tk.Button(root, text="Set Budget", command=set_budget).pack(pady=5)

# Expense Entry UI Elements
tk.Label(root, text="Expense Amount:").pack(pady=5)
amount_entry = tk.Entry(root, width=20)
amount_entry.pack()

tk.Label(root, text="Expense Description:").pack(pady=5)
description_entry = tk.Entry(root, width=20)
description_entry.pack()

tk.Label(root, text="Category:").pack(pady=5)
categories = ["Groceries", "Entertainment", "Transport", "Bills", "Others"]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

# Additional Buttons
tk.Button(root, text="Show Expense Distribution", command=show_category_distribution).pack(pady=10)
tk.Button(root, text="Monthly Summary", command=monthly_summary).pack(pady=10)
tk.Button(root, text="Export to CSV", command=export_to_csv).pack(pady=10)

root.mainloop()
