from turtle import Turtle
SNAKE_SPEED = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITION = [(0,0) , (-20,0) , (-40,0) ]

class Snake:
    # TODO 생성자를 수정하세요.
    """
    snake_body list 초기화
    create_snake() 호출
    self.head를 snake_body의 첫 번째 요소로 지정
    """
    def __init__(self):
        self.snake_body= None

        self.head = None


    # TODO 함수 수정
    """
    add_segment 함수 호출 starting position의 수 만큼
    """
    def create_snake(self):
        pass


    # TODO 함수 수정
    """
    새로운 터틀을 생성후 세크먼트로서 snake_body에 추가하기
    흰색이고 펜 들고 특정 위치로 이동하기
    """
    def add_segment(self , position):
        new_segment = Turtle('square')
        '''구현할 것
        '''
        self.snake_body.append(new_segment)


        


    def extend(self ):
        # Add a new segment to the snake
        self.add_segment(self.snake_body[-1].position())

    def move(self):
    
        for seg_num in range(len(self.snake_body) - 1 , 0 , -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x , new_y)
    
        self.head.forward(SNAKE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    