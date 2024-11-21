# Student Performance Tracker

## **Table of Contents**
1. [Introduction](#introduction)  
2. [Project Features](#project-features)  
3. [Technologies Used](#technologies-used)  
4. [Setup Instructions](#setup-instructions)  
5. [Project Structure](#project-structure)  
6. [Usage Guide](#usage-guide)  
    - [Managing Subjects](#managing-subjects)  
    - [Adding Grades](#adding-grades)  
    - [Viewing Performance Trends](#viewing-performance-trends)   
7. [Future Enhancements](#future-enhancements)  
8. [License](#license)  

---

## **Introduction**

The **Student Performance Tracker** is a Python-based desktop application built with Tkinter. It provides students, teachers, and educational institutions with an intuitive interface to:
- Manage subjects.
- Record and analyze grades.
- Visualize performance trends over semesters.

This project is designed to help students track their academic progress efficiently, providing both basic and advanced features like data storage using SQLite and trend visualization with Matplotlib.

---

## **Project Features**

1. **Subject Management**  
   - Add subjects to the database.  
   - View a list of all added subjects.  

2. **Grade Management**  
   - Add grades for specific subjects.  
   - Specify the semester for each grade entry.  
   - View all grades in a tabular format.  

3. **Performance Trends Visualization**  
   - Generate line charts to visualize performance trends for individual subjects across semesters.

4. **Data Persistence**  
   - All data (subjects, grades) is stored locally using SQLite for future reference.

5. **Responsive User Interface**  
   - Built with Tkinter to ensure simplicity and cross-platform compatibility.

---

## **Technologies Used**

### **Programming Language**
- Python (v3.x)

### **Libraries**
- **Tkinter**: For the GUI interface.
- **SQLite3**: For local database storage.
- **Matplotlib**: For creating performance trend visualizations.

### **Development Tools**
- **Python IDE**: Visual Studio Code / PyCharm (recommended).
- **Package Installer**: pip (to install required libraries).

---

## **Setup Instructions**

Follow these steps to set up and run the project on your local machine:

### **1. Clone the Repository**
Download or clone the repository using the following command:
```bash
git clone <repository_url>


### **2. Install Required Libraries**
Ensure you have Python installed (preferably v3.x). Install the necessary Python libraries using the following command:
```bash
pip install matplotlib
```

### **3. Run the Application**
Navigate to the project directory and run the application:
```bash
python final_app.py
```

---

## **Project Structure**

```
├── database.py           # Handles SQLite database operations
├── final_app.py          # Main Tkinter application file
├── README.md             # Documentation
└── requirements.txt      # List of required libraries
```

---

## **Usage Guide**

### **1. Managing Subjects**
   - Navigate to the **Subjects Tab**.
   - Add a subject using the text input field and click **"Add Subject"**.  
   - The subject will be stored in the database and displayed in the list below.

### **2. Adding Grades**
   - Navigate to the **Grades Tab**.  
   - Select a subject from the dropdown menu.  
   - Enter the grade and semester in the respective fields.  
   - Click **"Add Grade"** to save the information.  
   - All grades will be displayed in the tabular format.

### **3. Viewing Performance Trends**
   - Navigate to the **Performance Trends Tab**.  
   - Select a subject from the dropdown menu.  
   - Click **"Show Trend"** to generate a line chart.  
   - The chart visualizes grades across semesters.

---

## **Future Enhancements**

### **1. Additional Features**
   - Export data to CSV format.  
   - Import data from external files.  
   - Add student-specific profiles for personalized tracking.

### **2. Improved Analytics**
   - Display average grades per semester.  
   - Provide comparisons between subjects.  

### **3. UI Enhancements**
   - Add light/dark mode toggle.  
   - Make the application responsive for varying screen sizes.

### **4. Multi-User Functionality**
   - Enable a login system for multiple users with unique data.

---

## **License**

This project is licensed under the MIT License. You are free to use, modify, and distribute the software with proper attribution.
