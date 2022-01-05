from random import randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# CarManager is a Turtle as well to fix a bug, hence pen up and goto
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        # creates list that will be populated by the created cars
        self.all_cars = []
        self.pu()
        self.goto(-400,-400)
        self.move_distance = STARTING_MOVE_DISTANCE

    # creates the cars to spawn
    def create_car(self):
        # reduces the spawn rate so that it's not 1 spawn every 0.1 seconds
        random_chance = randint(1, 5)
        if random_chance == 1:
            # creates car with random color and y coordinate
            new_car = Turtle("square")
            new_car.settiltangle(270)
            new_car.shapesize(2,1,1)
            new_car.pu()
            new_car.color(COLORS[randint(0,5)])
            new_car.setpos(320,randint(-300,300))
            self.all_cars.append(new_car)

    # movement for all of the spawned cars    
    def car_move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)
    
    # speeds up the car by the chosen increment (upon level up)
    def speed_up(self):
        self.move_distance += MOVE_INCREMENT