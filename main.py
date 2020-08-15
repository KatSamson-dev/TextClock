import tkinter as tk
from datetime import datetime

hourString = ""
preWord = ""
preposition = ""
timeNow = ""
hourInt = 0
intMinute = 0

def clock():
    timeNow = datetime.now()
    tString =  ("%s:%s" % (timeNow.hour, timeNow.minute))
    hourInt = timeNow.hour
    intMinute = timeNow.minute
    return hourInt, intMinute

def fetchHour(hourInt):
    if hourInt == 0 or hourInt == 12:
        hourString = "Twelve"
    elif hourInt == 1 or hourInt == 13:
        hourString = "One"
    elif hourInt == 2 or hourInt == 14:
        hourString = "Two"
    elif hourInt == 3 or hourInt == 15:
        hourString = "Three"
    elif hourInt == 4 or hourInt == 16:
        hourString = "Four"
    elif hourInt == 5 or hourInt == 17:
        hourString = "Five"
    elif hourInt == 6 or hourInt == 18:
        hourString = "Six"
    elif hourInt == 7 or hourInt == 19:
        hourString = "Seven"
    elif hourInt == 8 or hourInt == 20:
        hourString = "Eight"
    elif hourInt == 9 or hourInt == 21:
        hourString = "Nine"
    elif hourInt == 10 or hourInt == 22:
        hourString = "Ten"
    elif hourInt == 11 or hourInt == 23:
        hourString = "Eleven"

    return hourString

def fetchMinute(intMinute):
    #set minute value to a multiple of 5
    intMinute = intMinute/5
    intMinute = round(intMinute)
    intMinute = intMinute*5

    if intMinute == 0:
        preWord = hourString
    if intMinute == 5 or intMinute == 55:
        preWord = "Five"
    if intMinute == 10 or intMinute == 50:
        preWord = "Ten"
    if intMinute == 15 or intMinute == 45:
        preWord = "Quarter"
    if intMinute == 20 or intMinute == 40:
        preWord = "Twenty"
    if intMinute == 25 or intMinute == 35:
        preWord = "Twenty Five"
    if intMinute == 30:
        preWord = "Half"

    return preWord


clockVal = clock()
if clockVal[1] > 30:
    hourString = fetchHour(clockVal[0] + 1)
else:
    hourString = fetchHour(clockVal[0])
preWord = fetchMinute(clockVal[1])
# set the preposition
if clockVal[1] <= 30:
    preposition = " Past "
elif clockVal[1] > 30:
    preposition = " To "
print(preWord + preposition + hourString)
