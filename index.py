import tkinter as tk
from tkinter import ttk
def calculate():
    import datetime
    year = n1.get()
    month = n2.get()
    day = n3.get()
    year = int(year)
    month = int(month)
    day = int(day)
    x = datetime.datetime.now()
    dateyear = x.year
    dateyears = x.year
    datemonth = x.month
    dateday = x.day
    leapyear = 0
    leap = True
    if month > datemonth:
        while leap == True:
            if dateyears > year:
                dateyears = dateyears - 4
                leapyear = leapyear + 1
            else:
                leap = False
        years = (dateyear-1) - year
        yeardays = (years * 365) + (leapyear - 1)
        months = (12 - month)+datemonth
        monthdays = months * 30
        if day <= dateday-1:
            days = dateday - day
        elif day > dateday-1:
            days = (30 - day)+dateday
    elif month < datemonth:
        while leap == True:
            if dateyears > year:
                dateyears = dateyears - 4
                leapyear = leapyear + 1
            else:
                leap = False
        years = dateyear - year
        yeardays = (years * 365) + (leapyear - 1)
        months = datemonth - month
        monthdays = months * 30
        if day <= dateday-1:
            days = dateday - day
        elif day > dateday-1:
            days = (30 - day)+dateday
    elif month == datemonth:
        if day <= dateday-1:
            while leap == True:
                if dateyears > year:
                    dateyears = dateyears - 4
                    leapyear = leapyear + 1
                else:
                    leap = False
            years = dateyear - year
            yeardays = (year * 365) + (leapyear - 1)
            months = datemonth - month
            monthdays = months * 30
            days = dateday - day
        elif day > dateday-1:
            while leap == True:
                if dateyears > year:
                    dateyears = dateyears - 4
                    leapyear = leapyear + 1
                else:
                    leap = False
            years = (dateyear-1) - year
            yeardays = (years * 365) + (leapyear - 1)
            months = (12 - month)+datemonth
            monthdays = months * 30
            days = (30 - day)+dateday
    totaldays = yeardays + monthdays + days
    answer["text"] = f"{totaldays}"
window = tk.Tk()
title1 = tk.Label(text="Year", bg = "orange", padx = 100)
title1.grid(row = 0, column = 0)
n1 = tk.Entry()
n1.grid(row = 1, column = 0)
title1 = tk.Label(text="Month", bg = "orange", padx = 100)
title1.grid(row = 0, column = 1)
n2 = tk.Entry()
n2.grid(row = 1, column = 1)
title1 = tk.Label(text="Day", bg = "orange", padx = 100)
title1.grid(row = 0, column = 2)
n3 = tk.Entry()
n3.grid(row = 1, column = 2)
calculatebutton = tk.Button(text = "Calculate", command = calculate)
calculatebutton.grid(row = 2, column = 1)
answer = tk.Label(text = "", relief = "groove")
answer.grid(row = 3, column = 1)
window.mainloop
