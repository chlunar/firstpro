
from tkinter import *
import random
app = Tk()
app.title("Hello World")

canvas_width = 800
canvas_height = 800

canvas = Canvas(app, width=canvas_width, height=canvas_height)
canvas.pack()


colors = ['purple', 'red', 'yellow', 'blue', 'pink', 'cyan', 'lightgray', 'pink', 'skyblue']
def f_rectangle(width, height, fill_color):
    x1 = random.randrange(width/2)
    y1 = random.randrange(height/2)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)

    canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color)


for i in range(10):
    f_rectangle(400, 400, colors[random.randrange(0,9)])

app.mainloop()
