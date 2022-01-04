from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.pu()
        self.goto(position)

    # movement functions for player controls
    def go_up(self):
        moving_y = self.ycor() + 20
        self.setpos(x=self.xcor(),y=moving_y)

    def go_down(self):
        moving_y = self.ycor() - 20
        self.setpos(x=self.xcor(),y=moving_y)

    
