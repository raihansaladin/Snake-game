from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pysnakes")

position = [(0, 0), (-20, 0), (-40, 0)]

for cor in position:
    turt = Turtle(shape="square")
    turt.color("white")
    turt.goto(cor)


screen.exitonclick()