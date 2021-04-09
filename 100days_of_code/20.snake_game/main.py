from turtle import Screen
from snake import Snake
import time

#setting up for window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to Snake Game !!!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')


#moving snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()