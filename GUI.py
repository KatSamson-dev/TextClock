from mainAlgos import *
from tkinter import *
from tkinter.ttk import *
from WeatherFetch import *
from PIL import Image, ImageTk


root = Tk()
root.title('SmartMirror')
root.geometry("568x320")
root.configure(bg = 'black')
def time():
    textTime = tellTime()
    lbl.config(text = textTime)
    lbl.after(1000, time)

#weather funcs
def weather():
    image,temp,description = getWeatherInfo(iconSet, current)
    temp = str(temp)
    tempLBL.config(text = temp+"°C")
    descLBL.config(text = description)
    image = image.resize((64,64),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel.config(image = img)
    panel.image = img


#timeLabels
#labelFill1 = Label(root, text="", background = 'black')
lbl = Label(root, font = ('calibri', 25, 'bold'), background = 'black', foreground = 'white')

#weather
tempLBL = Label(root, font = ('calibri', 20, 'bold'), background = 'black', foreground = 'white')
descLBL = Label(root, font = ('calibri', 25, 'bold'), background = 'black', foreground = 'white')
panel = Label(root, background = 'black', foreground = 'white')

#positioning
lbl.place(x = 20, y = 10)
#labelFill1.grid(row = 0, column = 1)

descLBL.place(x = 400, y = 60)
tempLBL.place(x = 400, y = 110)

panel.place(x=290,y=75,height=64,width=64)

#calls
time()
weather()

mainloop()



