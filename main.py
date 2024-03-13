from tkinter import *
import pandas as pd
import math
from tkinter import messagebox

# import changes calc file
changes = pd.read_csv("changes.csv")
dict_change = {row.Total: row.Change for (index, row) in changes.iterrows()}


# create function to calc paces
def calculate_goal_pace():
    total_seconds = float(minute_warm.get())*60 + float(second_warm.get())
    t_dp = float(dew_point_warm.get()) + float(temp_warm.get())
    percent = dict_change[t_dp]
    amount_change = (percent+100)/100
    new_pace_seconds = total_seconds * amount_change
    new_min = math.floor(new_pace_seconds/60)
    new_sec = int(new_pace_seconds % 60)
    # new pace label
    messagebox.showerror(title="Adjusted Pace", message=f"The adjusted pace is: {new_min}:{new_sec}/mile")


def calculate_faster_pace():
    total_seconds = float(minute_cool.get())*60 + float(second_cool.get())
    t_dp = float(dew_point_cool.get()) + float(temp_cool.get())
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
goal_pace_warm = Label(text="Calculate Pace in Warmer Weather:")
goal_pace_warm.place(x=50, y=65)
# goal pace
goal_pace_cool = Label(text="Calculate Pace in Cooler Weather:")
goal_pace_cool.place(x=300, y=65)
# create entries for min and sec per mile
minute_warm = Entry(width=3)
minute_warm.place(x=100, y=100)
minute_cool = Entry(width=3)
minute_cool.place(x=350, y=100)
minute_warm.focus()
colon_warm = Label(text=":")
colon_warm.place(x=140, y=100)
colon_cool = Label(text=":")
colon_cool.place(x=390, y=100)
second_warm = Entry(width=3)
second_warm.place(x=150, y=100)
second_cool = Entry(width=3)
second_cool.place(x=400, y=100)
per_mile_warm = Label(text="/Mile")
per_mile_warm.place(x=190, y=100)
per_mile_cool = Label(text="/Mile")
per_mile_cool.place(x=440, y=100)
# create entries for climate
dew_point_warm = Entry(width=3)
dew_point_warm.place(x=180, y=150)
dew_point_cool = Entry(width=3)
dew_point_cool.place(x=430, y=150)
dew_point_label_warm = Label(text="Dew Point:")
dew_point_label_warm.place(x=100, y=150)
dew_point_label_cool = Label(text="Dew Point:")
dew_point_label_cool.place(x=350, y=150)
temp_warm = Entry(width=3)
temp_warm.place(x=200, y=190)
temp_cool = Entry(width=3)
temp_cool.place(x=450, y=190)
temp_label_warm = Label(text="Temperature:")
temp_label_warm.place(x=100, y=190)
temp_label_cool = Label(text="Temperature:")
temp_label_cool.place(x=350, y=190)
# create Adjust button
adjust = Button(text="Adjust", command=calculate_goal_pace)
adjust.place(x=100, y=225)
adjust = Button(text="Adjust", command=calculate_faster_pace)
adjust.place(x=350, y=225)

window.mainloop()
