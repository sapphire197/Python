import pytz
from datetime import datetime
import pickle

HISTORY_FILE = "timezone_history.pkl"

def load_history():
    try:
        with open(HISTORY_FILE, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE, "wb") as f:
        pickle.dump(history, f)

def convert_time():
    tz1 = input("Enter the first timezone (e.g., 'Asia/Kolkata'): ")
    tz2 = input("Enter the second timezone (e.g., 'America/New_York'): ")
    time_str = input("Enter the time to convert (YYYY-MM-DD HH:MM): ")
    
    try:
        tz1_zone = pytz.timezone(tz1)
        tz2_zone = pytz.timezone(tz2)
        local_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        local_time = tz1_zone.localize(local_time)
        
        converted_time = local_time.astimezone(tz2_zone)
        print(f"Time in {tz2}: {converted_time.strftime('%Y-%m-%d %H:%M')}")
        
        return {"from_tz": tz1, "to_tz": tz2, "from_time": time_str, "to_time": converted_time.strftime("%Y-%m-%d %H:%M")}
    except Exception as e:
        print(f"Error: {e}")
        return None

def view_history(history):
    if not history:
        print("No conversion history found.")
        return
    print("\n--- Conversion History ---")
    for i, entry in enumerate(history, start=1):
        print(f"{i}. {entry['from_time']} {entry['from_tz']} -> {entry['to_time']} {entry['to_tz']}")

def main():
    history = load_history()
    while True:
        print("\n--- Timezone Converter ---")
        print("1. Convert Time")
        print("2. View Conversion History")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            conversion = convert_time()
            if conversion:
                history.append(conversion)
                save_history(history)
        elif choice == "2":
            view_history(history)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
