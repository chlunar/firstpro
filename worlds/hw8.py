
from cs1robots import *
import random
load_world('./homework/finalMaze2.wld')

orient_dict = {0:'N', 1: 'E', 2: 'S', 3: 'W'}

initial_orient = random.randint(0,3)
gshs1 = Robot(color="light_blue", orientation=orient_dict[initial_orient], avenue=11, street=11)
gshs1.set_trace(color='blue')
gshs1.set_pause(1)

initial_orient = random.randint(0,3)
gshs2 = Robot(color="yellow", orientation=orient_dict[initial_orient], avenue=11, street=11)
gshs2.set_trace(color='blue')
gshs2.set_pause(1)

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def turn_around(robot):
    for i in range(2):
        robot.turn_left()


#To Do 1
with open("./homework/command.txt", "r") as f:
    command1 =
    command2 =

#To Do 2
command1 =
command2 =


# 주어진 경로가 circular인지 판단(출발지점으로 돌아오는지 체크) 해서 True, False Return
# 움직이는 것은 위의 command1, command2를 통해서 구현할 것
# 앞이 막혀 있는 상태에서 직진을 하려고 하면 뒤로 돈 후에 한칸 전진
# 앞이 막혀 있는 상태에서 좌회전, 우회전은 해당 움직임을 수행

# To do 3
def isCircular(x, y, dir, path, robot):


print(isCircular(11,11, initial_orient, command1, gshs1))
print(isCircular(11,11, initial_orient, command2, gshs2))

