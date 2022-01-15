from cs1robots import *
import random
load_world('finalMaze2.wld')

orient_dict = {0:'N', 1: 'E', 2: 'S', 3: 'W'}

initial_orient = random.randint(0,3)
gshs1 = Robot(color="light_blue", orientation=orient_dict[initial_orient], avenue=11, street=11)
gshs1.set_trace(color='blue')
gshs1.set_pause(0.1)

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def turn_around(robot):
    for i in range(2):
        robot.turn_left()

def go(path, robot):
    for i in range(len(path) - 1):
        if path[i] == 'M':
            if not robot.front_is_clear():
                turn_around(robot)
            robot.move()
        if path[i] == 'L':
            robot.turn_left()
        if path[i] == 'R':
            turn_right(robot)

with open("./homework/command2.txt", "r") as f:
    command_list = f.readlines()

for i in range(len(command_list)):
    command = list(command_list[i])
    go(command, gshs1)

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

def isCircular(x, y, dir, path, robot):
    for i in range(len(path)):
        command = list(path[i])
        for j in range(len(command)-1):
            if command[j]=='M':
                if (x==1 and dir==3) or (x==21 and dir==1) or (y==1 and dir==2) or (y==21 and dir==0):
                    dir=(dir+2)%4
                x+=dx[dir]
                y+=dy[dir]
            if command[j]=='L':
                dir=(dir+3)%4
            if command[j]=='R':
                dir=(dir+1)%4
    if x==11 and y==11:
        return True
    else:
        return False


print(isCircular(11,11, initial_orient, command_list, gshs1))