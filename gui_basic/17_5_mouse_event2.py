
from tkinter import *
import random
import time
app = Tk()
app.title("Hello World")

canvas_width = 500
canvas_height = 500

canvas = Canvas(app, width=canvas_width, height=canvas_height)
canvas.pack()

def draw(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="purple")

canvas.bind_all("<B1-Motion>", draw)
msg = Label(app, text="mouse drag")
msg.pack(side=BOTTOM)

app.mainloop()
sys.exit()

