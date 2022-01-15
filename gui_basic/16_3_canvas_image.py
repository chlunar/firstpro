
from tkinter import *
app = Tk()
app.title("Hello World")

canvas_width = 800
canvas_height = 800

canvas = Canvas(app, width=canvas_width, height=canvas_height)
canvas.pack()

img_gif = PhotoImage(file="gshs.gif")
canvas.create_image(0, 0, anchor=NW, image=img_gif)
canvas.create_text(40, 600, text="GSHS")


app.mainloop()
