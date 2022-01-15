
from tkinter import *
import random
import time
from math import *

app = Tk()
app.geometry('200x100+200+200')

def calc(event):
    label.configure(text= "Result: "+ str(eval(entry.get())))


Label(app, text= 'Input Text:').pack()

entry = Entry(app)
entry.bind("<Return>", calc)
entry.pack()

label=Label(app, text="result")
label.pack()

app.mainloop()
sys.exit()

