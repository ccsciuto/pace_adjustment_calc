from tkinter import *
import pandas as pd
import math
from tkinter import messagebox

# import changes calc file
changes = pd.read_csv("changes.csv")
dict_change = {row.Total: row.Change for (index, row) in changes.iterrows()}


# create function to calc paces
def calculate_goal_pace():
    total_seconds = float(minute.get())*60 + float(second.get())
    t_dp = float(dew_point.get()) + float(temp.get())
    percent = dict_change[t_dp]
    amount_change = (percent+100)/100
    new_pace_seconds = total_seconds * amount_change
    new_min = math.floor(new_pace_seconds/60)
    new_sec = int(new_pace_seconds % 60)
    # new pace label
    messagebox.showerror(title="Adjusted Pace", message=f"The adjusted pace is: {new_min}:{new_sec}/mile")


def calculate_faster_pace():
    total_seconds = float(minute.get())*60 + float(second.get())
    t_dp = float(dew_point.get()) + float(temp.get())
    percent = dict_change[t_dp]
    amount_change = (percent+100)/100
    new_pace_seconds = total_seconds / amount_change
    new_min = math.floor(new_pace_seconds/60)
    new_sec = int(new_pace_seconds % 60)
    # new pace label
    messagebox.showerror(title="Adjusted Pace", message=f"The adjusted pace is: {new_min}:{new_sec}/mile")


# create screen
window = Tk()
window.title("Pace Adjustment Calculator")
window.config(padx=20, pady=20)
window.minsize(width=600, height=300)
# create description box
description = Label(text="This calculator will adjustment goal paces according to different weather variables.\n"
                         "Enter a specific pace, dew point and temperature below, and click 'Adjust' to see\n"
                         "what the corresponding pace will be in the given climate.")
description.place(x=30, y=0)
# goal pace
goal_pace = Label(text="Goal Pace:")
goal_pace.place(x=100, y=65)
# create entries for min and sec per mile
minute = Entry(width=3)
minute.place(x=100, y=100)
minute.focus()
colon = Label(text=":")
colon.place(x=140, y=100)
second = Entry(width=3)
second.place(x=150, y=100)
per_mile = Label(text="/Mile")
per_mile.place(x=190, y=100)
# create entries for climate
dew_point = Entry(width=3)
dew_point.place(x=180, y=150)
dew_point_label = Label(text="Dew Point:")
dew_point_label.place(x=100, y=150)
temp = Entry(width=3)
temp.place(x=200, y=190)
temp_label = Label(text="Temperature:")
temp_label.place(x=100, y=190)
# create Adjust button
adjust = Button(text="Adjust", command=calculate_goal_pace)
adjust.place(x=100, y=225)

window.mainloop()
