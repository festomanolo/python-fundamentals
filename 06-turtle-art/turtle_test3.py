from turtle import *
colors = ["red", "green", "blue", "yellow"]
for i in range(299):
    pencolor(colors[i % 3])
    forward(i)
    backward(i)
    left(182)
    right(23)
    speed(2423)
