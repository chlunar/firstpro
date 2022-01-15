from tkinter import *
import random
import time


def close_window():
    global running
    running = False
    print("Close game")


app = Tk()
app.title("Simple Game")
app.protocol("WM_DELETE_WINDOW", close_window)

canvas = Canvas(app, width=500, height=500)
canvas.pack()
canvas.update()
scorelabel = Label(app, text="0")

class Ball:
    score = 0
    t = 0
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = self.canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 250, 0)
        self.start = random.random()*2+2
        self.x = self.start
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.hit_paddle = False

    def hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if(self.hit_paddle != True and pos[1] <= paddle_pos[3] and pos[3] >= paddle_pos[1] and pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0]):
            Ball.score += 1
            scorelabel.config(text=str(Ball.score))
            self.hit_paddle = True

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.hit(pos)
        if pos[1] <= 0:
            self.y = 3
            self.hit_paddle = False
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = self.start
        if pos[2] >= self.canvas_width:
            self.x = -self.start

    def create(self):
        if (Ball.t % 580 == 0 and Ball.t < 2000):
            ball = Ball(canvas, paddle, 'red')
            arr.append(ball)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 150, 400)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()

    def move(self, event):
        if event.keysym == "Left":
            self.x -= 5
        else:
            self.x += 5

    def draw(self):
        pos = self.canvas.coords(self.id)
        if(pos[0] <= 0):
            self.x *= -1
            self.canvas.move(self.id, -pos[0], 0)
        if(pos[2] >= 500):
            self.x *= -1
            self.canvas.move(self.id, 500 - pos[2], 0)
        self.canvas.move(self.id, self.x, self.y)
        self.x *= 0.9

paddle = Paddle(canvas, 'blue')
arr = []
ball = Ball(canvas, paddle, 'red')
arr.append(ball)
canvas.bind_all("<KeyPress-Left>", paddle.move)
canvas.bind_all("<KeyPress-Right>", paddle.move)
scorelabel.pack()

running = True
while running:
    if not running:
        break
    chk = True
    for ball in arr:
        if ball.hit_bottom == True:
            chk = False
    if chk == True:
        for ball in arr:
            ball.draw()
        Ball.t += 1
        ball.create()
        paddle.draw()
        app.update()
        time.sleep(0.01)
        continue

    running = False
    break

print("Your score: {0}".format(Ball.score))
sys.exit()