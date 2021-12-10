# import colorgram
from turtle import Turtle, Screen
import random

#  Code used initially to get the list of colors, then the background rgb values were removed
# colors = colorgram.extract('image.jpg', 15)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_turtle = (r, g, b)
#     rgb_colors.append(rgb_turtle)

# print(rgb_colors)
bert = Turtle()
screen = Screen()
# list of colors that the dots will randomly have
color_list = [(1, 9, 29), (121, 96, 42), (238, 211, 72), (77, 34, 23), (221, 80, 59),
 (225, 117, 100), (92, 1, 21), (178, 140, 171), (151, 92, 116), (35, 90, 26), (8, 154, 73)]
# initial x and y axis values so that the 10 x 10 painting fits well in the window
FIRST_Y = -150
FIRST_X = -150
# sets the colors to be read with 0-255 rgb values
screen.colormode(255)
bert.hideturtle()
bert.speed("fastest")
# draws a 10 x 10 dot painting
for i in range(10):
    bert.penup()
    bert.setposition(FIRST_X,FIRST_Y)
    for j in range(10):
        bert.color(random.choice(color_list))
        bert.dot(20)
        bert.penup()
        bert.fd(50)

    # increments the y axis so that the painting ends up 10 x 10 with even spaces in between
    FIRST_Y += 50

screen.exitonclick()
