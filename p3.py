from cs1robots import *
load_world('p3.wld')
gshs=Robot()
gshs.set_pause(0)

s={()}
dic={}

def f():
    lst=[]
    if gshs.get_pos() in s:
        gshs.turn_left()
        gshs.turn_left()
        gshs.move()
        return
    s.add(gshs.get_pos())

    if gshs.front_is_clear():
        gshs.move()
        lst.append(gshs.get_pos())
        f()
        gshs.turn_left()
        gshs.turn_left()
    gshs.turn_left()

    if gshs.front_is_clear():
        gshs.move()
        lst.append(gshs.get_pos())
        f()
        gshs.turn_left()
        gshs.turn_left()
    gshs.turn_left()

    if gshs.front_is_clear():
        gshs.move()
        lst.append(gshs.get_pos())
        f()
        gshs.turn_left()
        gshs.turn_left()
    gshs.turn_left()

    if gshs.front_is_clear():
        gshs.move()
        lst.append(gshs.get_pos())
        f()
        gshs.turn_left()
        gshs.turn_left()
    gshs.turn_left()

    dic[gshs.get_pos()]=lst

    gshs.turn_left()
    gshs.turn_left()
    if gshs.front_is_clear():
        gshs.move()

f()

a=int(input())
b=int(input())

que=[]
ch={()}
frm={}

que.append((1, 1))
ch.add((1, 1))

i=0
while i<len(que):
    for j in dic[que[i]]:
        if j not in ch:
            que.append(j)
            ch.add(j)
            frm[j]=que[i]
    i+=1

anslst=[]

target=(a, b)

anslst.append(target)
while target != (1, 1):
    target=frm[target]
    if target != (1, 1):
        anslst.append(target)
anslst.append((1, 1))
anslst.reverse()
print(anslst)

gshs2=Robot()
gshs2.set_trace(color='blue')
gshs2.set_pause(0)

for i in anslst:
    if i == (1, 1):
        continue
    npos=gshs2.get_pos()
    if i[0]-npos[0]==1:
        gshs2.move()
    if i[1]-npos[1]==1:
        gshs2.turn_left()
        gshs2.move()
        gshs2.turn_left()
        gshs2.turn_left()
        gshs2.turn_left()
    if i[0] - npos[0] == -1:
        gshs2.turn_left()
        gshs2.turn_left()
        gshs2.move()
        gshs2.turn_left()
        gshs2.turn_left()
    if i[1] - npos[1] == -1:
        gshs2.turn_left()
        gshs2.turn_left()
        gshs2.turn_left()
        gshs2.move()
        gshs2.turn_left()

print(len(anslst)-1)