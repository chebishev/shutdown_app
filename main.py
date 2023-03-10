import os
import sys
from datetime import datetime
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
today = datetime.today()
cal = Calendar(root, selectmode="day",
               year=today.year, month=today.month, day=today.day)

cal.pack(pady=20)


# getting selected date and current date
def grad_date():
    # making the date in integers in order to make it double digits on the print below
    month, day, year = [int(x) for x in cal.get_date().split("/")]
    date.config(text=f"Selected Date is: {day:02}.{month:02}.{year:02}\nNow is: {today.strftime('%d.%m.%Y %H:%M')}")


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Execute Tkinter
root.mainloop()
