
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
    if event.keysym == "Up":
        canvas.move(id1, 0,  -5)

    elif event.keysym == "Down":
        canvas.move(id1, 0, 5)

    elif event.keysym == "Left":
        canvas.move(id1, -5, 0)

    else:
        canvas.move(id1, 5, 0)


canvas.bind_all("<KeyPress-Up>", move_t)
canvas.bind_all("<KeyPress-Down>", move_t)
canvas.bind_all("<KeyPress-Left>", move_t)
canvas.bind_all("<KeyPress-Right>", move_t)


app.mainloop()
sys.exit()

