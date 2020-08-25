from Clock2Text import *

def tellTime():
    clockVal = fetchTime()
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

    if clockVal[1] == 0:
        textTime = "It Is \n\n" + hourString
        return textTime
    textTime = "It Is \n\n" + preWord + preposition + "\n\n" + hourString

    return textTime

textTime = tellTime()
print(textTime)

