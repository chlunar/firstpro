
from tkinter import *
import random
import time
app = Tk()
app.title("Hello World")

canvas_width = 500
canvas_height = 500

canvas = Canvas(app, width=canvas_width, height=canvas_height)
canvas.pack()


id1 = canvas.create_polygon(10,10,10,60,50,35)

def move_t(event):
    canvas.move(id1, 10,10)

canvas.bind_all("<KeyPress-Return>", move_t)





app.mainloop()

