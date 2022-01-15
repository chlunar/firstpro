from turtle import Turtle

SNAKE_SPEED = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        print("set head right")
        self.head.color('green')

    def create_snake(self):
        self.add_segment(STARTING_POSITION[0])
        self.add_segment(STARTING_POSITION[1])
        self.add_segment(STARTING_POSITION[2])

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):

        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

        self.head.forward(SNAKE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            print("up")

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            print("down")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            print("left")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            print("right")
