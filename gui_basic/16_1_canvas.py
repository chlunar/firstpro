
from tkinter import *
app = Tk()
app.title("Hello World")

canvas_width = 200
canvas_height = 200

canvas = Canvas(app, width=canvas_width, height=canvas_height)
canvas.pack()

points = [0, 0, canvas_width, canvas_height/2, 0, canvas_height]
canvas.create_polygon(points, outline="green", fill="yellow", width=4)

app.mainloop()
