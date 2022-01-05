from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        # gives the turtle it's shape
        self.shape("turtle")
        self.color("#90EE90")
        self.settiltangle(90)
        self.pu()
        self.setpos(STARTING_POSITION)

    # moves the turtle the set distance (on up key press)
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(x=0, y=new_y)
    # brings turtle back to beginning coords
    def reset(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            