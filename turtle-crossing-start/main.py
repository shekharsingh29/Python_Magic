import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(turtle_player.move_ahead,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    
    # Detect colloision with cars
    for car in cars.all_cars:
        if car.distance(turtle_player) < 22:
            game_is_on = False
    
    # Detect turtle reaching the top
    if turtle_player.ycor() > 290:
        turtle_player.goto((0, -280))
        cars.increase_speed()
        score.update_scoreboard()


score.game_over()
screen.exitonclick()
