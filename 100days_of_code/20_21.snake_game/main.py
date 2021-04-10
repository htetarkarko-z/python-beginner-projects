from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# setting up for window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to Snake Game !!!")
screen.tracer(0)

# assign objects for snake, food and scoreboard
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# get user input from keyboard and assign it respectively
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

# moving snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < - 280 \
            or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < - 280:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with own body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
