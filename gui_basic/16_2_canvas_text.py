import numpy as np
from tkinter import *
app = Tk()
app.title("Hello World")

canvas_width = 200
canvas_height = 200

canvas = Canvas(app, width=canvas_width, height=canvas_height)
canvas.pack()
a=[0]
for i in range(200):
    a.append(i+1)
canvas.create_polygon(points, outline="green", fill="yellow", width=4)
canvas.create_text(100,100, text="Hello Tkinter", font=("Comic Sans MS", 15))

app.mainloop()
