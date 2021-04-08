import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
y_postion = -100

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_postion)
    y_postion += 50
    turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You won! {wining_color} is the winner")
            else:
                print(f"You lost. {wining_color} is the winner")

        random_distance= random.randint(0, 10)
        turtle.forward(random_distance)





screen.exitonclick()