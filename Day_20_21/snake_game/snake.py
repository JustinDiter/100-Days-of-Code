from turtle import Turtle

X_POSITION = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_LENGTH = 3

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.creation()
        self.head = self.snake_parts[0]


    def creation(self):
        '''creates the snake out of white squares'''
        for snake_part in range(SNAKE_LENGTH):
            self.create_segment()

    def create_segment(self):
        global X_POSITION
        snake_part = Turtle()
        snake_part.color("white")
        snake_part.shape("square")
        snake_part.pu()
        snake_part.setx(X_POSITION)
        X_POSITION -= 20
        self.snake_parts.append(snake_part)

    def extend(self):
        self.create_segment()

    def movement(self):
        '''the movement function for the snake, has the snake parts swap 
        positions from last part to first'''
        for snake_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_num - 1].xcor()
            new_y = self.snake_parts[snake_num - 1].ycor()
            self.snake_parts[snake_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        '''moves up with up arrow'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        '''moves down with down arrow'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    


    def left(self):
        '''moves left with left arrow'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        '''moves right with right arrow'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

            