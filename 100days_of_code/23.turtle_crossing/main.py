import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up the window
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# create player and car_manager objects
player = Player()
car_manager = CarManager()
score_board = Scoreboard()
# listen user input
screen.listen()
screen.onkey(fun=player.go_up, key='Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()