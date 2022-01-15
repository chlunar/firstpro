
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
id2 = canvas.create_polygon(20,20,60,60,50,35, fill="yellow")


for i in range(60):
    canvas.move(id1, 5, 5)
    canvas.move(id2, 15, 15)

    app.update()
    time.sleep(0.05)

app.mainloop()

