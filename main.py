import time
from turtle import Screen
from player import  Player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager= CarManager()
score=Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.move_up,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor()>300:
        player.goto(STARTING_POSITION)
        score.level_refresh()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
           game_is_on=False
           score.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.call_level_up()
        score.level_refresh()

screen.exitonclick()