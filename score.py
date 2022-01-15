from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.refresh_score()

    def refresh_score(self):
        self.score += 1
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 200)
        self.clear()
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, ALIGNMENT, FONT)
