
from tkinter import *
import random
import time
app = Tk()
app.geometry('200x100+200+200')

def click():
    label.configure(text=entry.get())
    btn.configure(text=entry.get())
    pass

label = Label(app, text= 'Input Text:')
label.grid(column=0, row=0)

entry = Entry(app, width=20)
entry.grid(column=0, row=1)

btn=Button(app, text="Change", command=click)
btn.grid(column=0, row=2)

app.mainloop()
sys.exit()

