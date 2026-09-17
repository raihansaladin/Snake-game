from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race Bet", prompt="Pick a color to bet!")
print(user_bet)
color_list = ["red", "green", "yellow", "pink", "purple", "orange"]
y_positions = [-120, -70, -20, 30, 80, 130]
all_turtles = []

if user_bet:
    race_is_on = True

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! the color you pick {winning_color} is won")
            else:
                print(f"You lose! the color who won is {winning_color}")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)


screen.exitonclick()