# Daily Mood Tracker with Data Visualization

The **Daily Mood Tracker** is a Python app that allows users to log their daily mood and displays mood trends over time through a graph. It uses Tkinter for the user interface, Matplotlib for graphing mood trends, and JSON for data storage.

## Features

- **Mood Logging**: Track mood daily by entering a mood level (1-10).
- **Data Visualization**: Visualize your mood trend over time with a line graph.
- **Persistent Data**: Stores mood entries in a JSON file for continuity.

## Data Storage
Mood entries are stored in a `mood_data.json` file in the following format:

```json
{
    "2024-01-01": "5",
    "2024-01-02": "7"
}
```

## Dependencies

- `tkinter` - For the GUI
- `matplotlib` - For displaying the mood trend graph

## Installation

Install the required dependencies by running the following command:

```bash
pip install matplotlib
```

## Usage

1. **Run the application**.
2. **Add a Mood**: Enter a mood level between 1 and 10 to represent your emotional state for the day.
3. **View Mood Trend**: Click on "Show Mood Graph" to display a graphical representation of your mood trend over time.

---
