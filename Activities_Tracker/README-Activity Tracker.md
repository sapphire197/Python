# Activity Tracker

The **Activity Tracker** is a simple GUI-based application that allows users to keep track of their activities.<br>
It uses Python's `tkinter` for the user interface and stores activities in a JSON file. Each activity is stored with a timestamp of when it was added.

## Features

- **Add Activity**: Users can add new activities with a timestamp.
- **View Activities**: Display all activities added so far.
- **Persistent Storage**: Activities are saved in a JSON file, so they are preserved between sessions.
- **User-Friendly Interface**: Simple and clean UI using `tkinter`.

## How It Works

1. The user enters an activity name in the input field and clicks the "Add Activity" button.
2. The activity is added to a list and displayed in the activity listbox.
3. The application saves the activities into a JSON file (`activities.json`) located in the specified directory, so data is not lost when the application is closed.
4. The user can view all activities by clicking the "Show All Activities" button, which displays the activities in a message box.

## Requirements

- **Python 3.x**
- **tkinter** (usually included in standard Python installations)
- **json** (standard library module)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo-url/activity-tracker
   ```

2. **Navigate to the project folder:**

   ```bash
   cd activity-tracker
   ```

3. **Run the application:**

   ```bash
   python activity_tracker_json.py
   ```

## Folder Structure

```
Activity Tracker
│
├── activity_tracker_json.py   # Main application file
├── activities.json       # File where activities are stored (automatically created)
└── README.md             # Documentation file
```

## How to Use

1. **Add an Activity**: 
   - Enter the activity name in the input box and click "Add Activity."
   - The activity will be displayed in the listbox and saved to the JSON file.

2. **View All Activities**: 
   - Click on "Show All Activities" to see a list of all the activities you have added so far.

## Configuration

The default location of the `activities.json` file can be set in the code using the `ACTIVITY_FILE` path. <br>
You can modify this path to point to a different directory if needed.

## JSON File Structure

The `activities.json` file stores all added activities in the following format:

```json
[
    {
        "name": "Example Activity",
        "timestamp": "2024-10-17 14:30:00"
    },
    {
        "name": "Another Activity",
        "timestamp": "2024-10-17 15:45:00"
    }
]
```

## Example Usage

1. Enter an activity, e.g., "Read a book."
2. Click "Add Activity."
3. The activity will appear in the list, and the timestamp will be recorded.

## Future Enhancements

- **Edit Activity**: Ability to edit existing activities.
- **Delete Activity**: Option to delete specific activities.
- **Search Functionality**: Search for specific activities based on keywords.
- **Export to CSV**: Allow exporting activities to a CSV file.

---
