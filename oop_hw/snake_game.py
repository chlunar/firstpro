from score import Score
from turtle import Screen , Turtle, position
import random
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Gshs Snake Game")

#그려지는 과정을 보이지 않고 한 번에 빠르게
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()

game_is_on = True

screen.update()

#TODO 키보드 이벤트 처리
#Up, Down, Left, Right에 따라 snake의 up down left right 함수 호출 매핑
'''
작성할 것.
'''

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #TODO Food와 충돌 처리 구현
    if snake.head.distance(food) < 15 :
        '''
        Food 접촉시 처리되어야할 작업 작성
        food refresh
        scroe board update
        snake extend
        '''
        pass

    # TODO Wall과의 충돌 처리 구현
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        '''
        게임 상태 False
        score board game over
        '''

    # TODO snake의 head와 tail과의 충돌 처리 구현

    for segment in snake.snake_body[1:]:
        pass
   

#클릭시 종료
screen.exitonclick()