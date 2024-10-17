import random
import json

STOCK_DATA = {
    "AAPL": {"price": 150, "trend": random.uniform(-1, 1)},
    "GOOGL": {"price": 2800, "trend": random.uniform(-1, 1)},
    "AMZN": {"price": 3500, "trend": random.uniform(-1, 1)},
    "TSLA": {"price": 700, "trend": random.uniform(-1, 1)}
}

PORTFOLIO_FILE = "portfolio.json"

def load_portfolio():
    try:
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"cash": 10000, "stocks": {}}

def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f)

def display_stocks():
    print("\n--- Stock Prices ---")
    for stock, data in STOCK_DATA.items():
        print(f"{stock}: ${data['price']:.2f}")

def buy_stock(portfolio):
    stock = input("Enter stock symbol to buy: ").upper()
    if stock not in STOCK_DATA:
        print("Invalid stock symbol.")
        return

    quantity = int(input(f"Enter quantity of {stock} to buy: "))
    cost = STOCK_DATA[stock]["price"] * quantity

    if portfolio["cash"] >= cost:
        portfolio["cash"] -= cost
        portfolio["stocks"].setdefault(stock, 0)
        portfolio["stocks"][stock] += quantity
        print(f"Bought {quantity} shares of {stock} for ${cost:.2f}.")
    else:
        print("Not enough cash.")

def sell_stock(portfolio):
    stock = input("Enter stock symbol to sell: ").upper()
    if stock not in portfolio["stocks"]:
        print("You don't own any shares of this stock.")
        return

    quantity = int(input(f"Enter quantity of {stock} to sell: "))
    if quantity > portfolio["stocks"][stock]:
        print("You don't own enough shares to sell.")
        return

    sale_value = STOCK_DATA[stock]["price"] * quantity
    portfolio["cash"] += sale_value
    portfolio["stocks"][stock] -= quantity
    if portfolio["stocks"][stock] == 0:
        del portfolio["stocks"][stock]

    print(f"Sold {quantity} shares of {stock} for ${sale_value:.2f}.")

def view_portfolio(portfolio):
    print("\n--- Portfolio ---")
    print(f"Cash: ${portfolio['cash']:.2f}")
    for stock, quantity in portfolio["stocks"].items():
        stock_value = STOCK_DATA[stock]["price"] * quantity
        print(f"{stock}: {quantity} shares (Value: ${stock_value:.2f})")

def update_stock_prices():
    for stock in STOCK_DATA:
        STOCK_DATA[stock]["price"] += STOCK_DATA[stock]["trend"] * random.uniform(1, 5)
        STOCK_DATA[stock]["price"] = max(STOCK_DATA[stock]["price"], 0.01)  # Prevent negative prices

def main():
    portfolio = load_portfolio()
    while True:
        update_stock_prices()
        display_stocks()

        print("\n--- Menu ---")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            buy_stock(portfolio)
        elif choice == "2":
            sell_stock(portfolio)
        elif choice == "3":
            view_portfolio(portfolio)
        elif choice == "4":
            save_portfolio(portfolio)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
