
from tkinter import *
app = Tk()
app.title("Hello World")

canvas = Canvas(app, width=400, height=200)
canvas.pack()

canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="blue")
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="yellow")



app.mainloop()
