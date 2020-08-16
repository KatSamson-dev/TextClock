from mainAlgos import *
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('SmartMirror')
root.geometry("568x640")
root.configure(bg = 'black')

def time():
    textTime = tellTime()
    lbl.config(text = textTime)
    lbl.after(1000, time)

labelFill1 = Label(root, text="", background = 'black')
lbl = Label(root, font = ('calibri', 25, 'bold'), background = 'black', foreground = 'white')

lbl.grid(row = 0, column = 0)
labelFill1.grid(row = 0, column = 1)

time()

mainloop()



