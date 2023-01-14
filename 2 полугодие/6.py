from turtle import *
left(90)
for i in range(7):
    forward(100)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*10,y*10)
        dot(5)
done()
