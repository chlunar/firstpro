from score import Score
from turtle import Screen, Turtle, position
import random
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gshs Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()

game_is_on = True

screen.update()

while game_is_on:
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.refresh_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    for segment in snake.snake_body[1:]:
        if snake.head.pos() == segment.pos():
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
