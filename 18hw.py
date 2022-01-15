from tkinter import *
import random
import time

app = Tk()
app.title("Bouncing Ball")

canvas = Canvas(app, width=500, height=500)
canvas.pack()
canvas.update()

colors = ['purple', 'red', 'yellow', 'blue', 'pink', 'cyan', 'lightgray', 'pink', 'skyblue']
class Ball:
    def __init__(self):
        self.r = random.random()*20+20
        self.vx = random.random()*20-10
        self.vy = random.random()*20-10
        self.b = canvas.create_oval(250-self.r, 250-self.r, 250+self.r, 250+self.r, fill=(colors[random.randrange(0,9)]))

    def go(self):
        canvas.move(self.b, self.vx, self.vy)
        self.vy += 0.1
        pos = canvas.coords(self.b)
        if(pos[1] < 0):
            self.vy *= -0.9
            canvas.move(self.b, 0, -pos[1])
        if(pos[3] > 500):
            self.vy *= -0.9
            canvas.move(self.b, 0, 500 - pos[3])
        if(pos[0] < 0):
            self.vx *= -0.9
            canvas.move(self.b, -pos[0], 0)
        if(pos[2] > 500):
            self.vx *= -0.9
            canvas.move(self.b, 500 - pos[2], 0)

arr=[]
for i in range(10):
    ball = Ball()
    arr.append(ball)

while True:
    app.update()
    for i in arr:
        i.go()
    time.sleep(0.01)

app.mainloop()
sys.exit()