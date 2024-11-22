import calendar
from tkinter import *
from tkinter import ttk, messagebox

# Function to show the calendar for a given month and year
def show_calendar():
    try:
        year = int(year_input.get())
        month = int(month_input.get())
        if 1 <= month <= 12:
            cal_text = calendar.TextCalendar().formatmonth(year, month)
            cal_display.config(state='normal')
            cal_display.delete(1.0, END)
            cal_display.insert(INSERT, cal_text)
            cal_display.config(state='disabled')
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid month (1-12).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for year and month.")

# Function to clear the calendar display and inputs
def clear_inputs():
    year_input.delete(0, END)
    month_input.delete(0, END)
    cal_display.config(state='normal')
    cal_display.delete(1.0, END)
    cal_display.config(state='disabled')

# Main Application Window
app = Tk()
app.title("GUI Calendar")
app.geometry("400x500")
app.resizable(False, False)

# Title Label
title_label = Label(app, text="GUI Calendar", font=("Arial", 20, "bold"), fg="blue")
title_label.pack(pady=10)

# Input Frame for Year and Month
input_frame = Frame(app)
input_frame.pack(pady=10)

year_label = Label(input_frame, text="Year: ", font=("Arial", 12))
year_label.grid(row=0, column=0, padx=5, pady=5)
year_input = Entry(input_frame, font=("Arial", 12), width=10)
year_input.grid(row=0, column=1, padx=5, pady=5)

month_label = Label(input_frame, text="Month: ", font=("Arial", 12))
month_label.grid(row=1, column=0, padx=5, pady=5)
month_input = Entry(input_frame, font=("Arial", 12), width=10)
month_input.grid(row=1, column=1, padx=5, pady=5)

# Buttons for Show Calendar and Clear
button_frame = Frame(app)
button_frame.pack(pady=10)

show_button = Button(button_frame, text="Show Calendar", font=("Arial", 12), command=show_calendar, bg="green", fg="white")
show_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", font=("Arial", 12), command=clear_inputs, bg="red", fg="white")
clear_button.grid(row=0, column=1, padx=10)

# Text Widget to Display the Calendar
cal_display = Text(app, font=("Courier", 12), width=40, height=10, state='disabled', bg="#f0f0f0")
cal_display.pack(pady=10)

# Footer Label
footer_label = Label(app, text="Made with Python and Tkinter", font=("Arial", 10), fg="gray")
footer_label.pack(side=BOTTOM, pady=10)

# Run the application
app.mainloop()
