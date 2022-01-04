from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setpos(x=0,y=0)
        self.pu()
        # movement attributes to manipulate during play
        self.x_move = 7
        self.y_move = 7

    # ball movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        
    # allows the ball to change directions
    def bounce_walls(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    # function to bring ball back to center and change direction to opposite paddle
    def reset_ball(self):
        self.setpos(x=0,y=0)
        self.bounce_paddle()
        self.move()