import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")

def clock():
    timeNow = datetime.now()
    tString =  ("%s:%s" % (timeNow.hour, timeNow.minute))
    print(timeNow.hour)
    w.config(text = tString, )
    root.after(1000, clock)

    return timeNow

def fetchHour(timeNow):
    hourString = ""
    if timeNow.hour == "00" or timeNow == "12":
        hourString = "Twelve"
    elif timeNow.hour == "01" or timeNow == "13":
        hourString = "One"
    elif timeNow.hour == "02" or timeNow == "14":
        hourString = "Two"
    elif timeNow.hour == "03" or timeNow == "15":
        hourString = "Three"
    elif timeNow.hour == "04" or timeNow == "16":
        hourString = "Four"
    elif timeNow.hour == "05" or timeNow == "17":
        hourString = "Five"
    elif timeNow.hour == "06" or timeNow == "18":
        hourString = "Six"
    elif timeNow.hour == "07" or timeNow == "19":
        hourString = "Seven"
    elif timeNow.hour == "08" or timeNow == "20":
        hourString = "Eight"
    elif timeNow.hour == "09" or timeNow == "21":
        hourString = "Nine"
    elif timeNow.hour == "10" or timeNow == "22":
        hourString = "Ten"
    elif timeNow.hour == "11" or timeNow == "23":
        hourString = "Eleven"

    return hourString

def fetchMinute(timeNow, hourString):
    #set minute value to a multiple of 5
    intMinute = int(timeNow.minute)
    intMinute = intMinute/5
    intMinute = round(intMinute)
    intMinute = intMinute*5
    strMinute = ""
    convTime = ""
    if intMinute <= 30:
        if intMinute == 0:
            convTime = hourString
            return convTime
        if intMinute == 5:
            convTime = "Five Past " + hourString
        if intMinute == 10:
            convTime = "Ten Past " + hourString
        if intMinute == 15:
            convTime = "Quarter Past " + hourString
        if intMinute == 20:
            convTime = "Twenty Past " + hourString
        if intMinute == 25:
            convTime = "Twenty Five Past " + hourString
        if intMinute == 30:
            convTime = "Half Past " + hourString

w = tk.Label(font = (100))
w.pack()
clock()
root.mainloop()
