from tkinter import *
import pandas as pd
import math
from tkinter import messagebox

# import changes calc file
changes = pd.read_csv("changes.csv")
dict_change = {row.Total: row.Change for (index, row) in changes.iterrows()}


# create function to calc paces
def calculate_warmer_pace():
    total_seconds = float(minute.get()) * 60 + float(second.get())
    t_dp = float(dew_point.get()) + float(temp.get())
    percent = dict_change[t_dp]
    amount_change = (percent+100)/100
    new_pace_seconds = total_seconds * amount_change
    new_min = math.floor(new_pace_seconds/60)
    new_sec = int(new_pace_seconds % 60)
    if new_sec < 10:
        new_sec = f"0{new_sec}"
        # new pace label
    messagebox.showinfo(title="Adjusted Pace", message=f"The adjusted pace is: {new_min}:{new_sec}/mile")


def calculate_cooler_pace():
    total_seconds = float(minute.get()) * 60 + float(second.get())
    t_dp = float(dew_point.get()) + float(temp.get())
    percent = dict_change[t_dp]
    amount_change = (percent+100)/100
    new_pace_seconds = total_seconds / amount_change
    new_min = math.floor(new_pace_seconds/60)
    new_sec = int(new_pace_seconds % 60)
    if new_sec < 10:
        new_sec = f"0{new_sec}"
    # new pace label
    messagebox.showinfo(title="Adjusted Pace", message=f"The adjusted pace is: {new_min}:{new_sec}/mile")


# create screen
window = Tk()
window.title("Pace Adjustment Calculator")
window.config(padx=20, pady=20)
window.minsize(width=600, height=300)
# create description box
description = Label(text="This calculator will adjustment goal paces according to different weather variables.\n"
                         "Enter a specific pace, dew point and temperature below, and click 'Adjust' to see\n"
                         "what the corresponding pace will be in the given climate.")
description.place(x=30, y=20)
# create entries for min and sec per mile
minute = Entry(width=3)
minute.place(x=225, y=100)
minute.focus()
colon_warm = Label(text=":")
colon_warm.place(x=265, y=100)
second = Entry(width=3)
second.place(x=275, y=100)
per_mile_warm = Label(text="/Mile")
per_mile_warm.place(x=315, y=100)
# create entries for climate
dew_point = Entry(width=3)
dew_point.place(x=300, y=140)
dew_point_label_warm = Label(text="Dew Point:")
dew_point_label_warm.place(x=225, y=140)
temp = Entry(width=3)
temp.place(x=315, y=180)
temp_label_warm = Label(text="Temperature:")
temp_label_warm.place(x=215, y=180)
# create Adjust button
adjust = Button(text="Adjust for warmer weather", command=calculate_warmer_pace)
adjust.place(x=50, y=215)
adjust = Button(text="Adjust for cooler weather", command=calculate_cooler_pace)
adjust.place(x=325, y=215)
window.mainloop()
