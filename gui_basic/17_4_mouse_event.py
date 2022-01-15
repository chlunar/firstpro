
from tkinter import *
import random
import time
app = Tk()
app.title("Hello World")


def motion(event):
    print("Mouse {} {} ".format(event.x, event.y))


msg = Message(app, text="Whatever\n you do")
msg.config(bg="lightgray", font=("Comic Sans MS", 24))
msg.bind("<Motion>", motion)
msg.pack()


app.mainloop()
sys.exit()

