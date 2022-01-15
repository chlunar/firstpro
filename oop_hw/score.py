from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier",24,'normal')

class Score(Turtle):
    # TODO 생성자를 수정하세요.
    """
    상위 클래스의 생성자 호출
    초기 점수 -1로
    refresh_score() 호출
    """
    def __init__(self):
        pass

    # TODO 함수 수정
    """
    점수 1 증가
    터틀 감추기
    흰색 
    펜업
    상단의 적절한 위치로 점수 이동
    점수 표시
    """
    def refresh_score(self):
        self.write(f"Score: {self.score} " , False , ALIGNMENT, FONT)

    # TODO 함수 수정
    """
    화면 중앙으로 이동후 게임 오버 표시
    """
    def game_over(self):
        pass
        