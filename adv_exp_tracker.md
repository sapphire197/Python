# Advanced Expense Tracker with Budget Alerts and Visualization

This **Advanced Expense Tracker** is a Python application to track expenses by category, manage budgets, view spending trends, and generate monthly summary reports with visualizations.

## Features

- **Monthly Budget Setting**: Define a monthly budget for tracking expenses.
- **Categorized Expense Logging**: Assign categories to expenses (e.g., Groceries, Bills, etc.).
- **Budget Alerts**: Receive alerts if total expenses exceed the monthly budget.
- **Expense Distribution Visualization**: View a pie chart of expenses by category.
- **Monthly Summary Report**: Shows total expenses, budget, and remaining balance.
- **Data Export to CSV**: Export all expenses to a CSV file for external analysis.


## Usage

1. **Set Budget**: Enter a budget for the month.
2. **Add Expenses**: Input the expense amount, description, and category.
3. **View Distribution**: Click "Show Expense Distribution" to view spending by category.
4. **Monthly Summary**: View total expenses, budget, and remaining balance for the month.
5. **Export Data**: Save all expenses to a CSV file.

## Data Storage

Expense data is stored in `advanced_expense_data.json` in the following format:

```json
{
    "budget": 1000,
    "expenses": [
        {"amount": 100, "description": "Groceries", "category": "Food", "date": "2024-10-05"},
        {"amount": 50, "description": "Internet", "category": "Bills", "date": "2024-10-06"}
    ]
}
```

## Dependencies

- `tkinter` - For the graphical user interface
- `matplotlib` - For visualizing expense distribution
- `csv` - To export data to a CSV file

Install dependencies using:

```bash
pip install matplotlib
```
