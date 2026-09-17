from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pysnakes")
screen.tracer(0)

position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for cor in position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(cor)
    segments.append(new_segment)


game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1 ): #Start = 2, Stop = 0, Step = -1
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()