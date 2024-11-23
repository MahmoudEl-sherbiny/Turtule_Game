import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    #  Detect collision turtle with cars
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            score.game_is_over()
            game_is_on = False

    # Detect when the turtle reaches the other side
    if turtle.is_at_finish_line():
        turtle.reset_position()
        cars.increase_speed()
        score.level_up()


screen.exitonclick()

