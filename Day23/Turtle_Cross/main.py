import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Window configuration
screen = Screen()
screen.setup(width=600, height= 600)
screen.title("Turtle Cross")
screen.tracer(0)
screen.bgcolor("#807E78")
screen.listen()

# Calling the accessory classes
player_turtle = Player()
scoreboard = Scoreboard()
cars = CarManager()

# shows the controls on the screen for the first level
scoreboard.write_controls()

# game loop flag
game_is_on = True

# game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    
    # player only control, up arrow to move forwards
    screen.onkeypress(player_turtle.move, "Up")

    # spawns the cars and moves them across the screen
    cars.create_car()
    cars.car_move()

    # if the turtle touches any of the cars => game over
    for car in cars.all_cars:
        if car.distance(player_turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    # level up if the player reaches the other side, reset coords and cars speed up
    if player_turtle.ycor() >= 280:
        player_turtle.reset()
        scoreboard.level += 1
        scoreboard.write_level()
        cars.speed_up()

screen.exitonclick()
