from turtle import Turtle
import random

class Food(Turtle):
    # TODO 생성자를 수정하세요.
    """
    상위 클래스의 생성자 호출
    모양을 원으로 수정
    펜 업~
    색상은 마음대로
    스피드는 가장 빠르게
    생성자에서 refresh 호출하기
    """
    def __init__(self):
       self.shapesize(stretch_len=0.5 , stretch_wid=0.5)

    # TODO 함수 수정
    """
    음식의 초기 위치를 랜덤하게 결정하세요(화면의 크기를 고려해서 적절하게
    그리고 Food의 위치를 해당 위치로 이동 시키세요. 
    """

    def refresh(self):
        self.goto(0, 0)