from turtle import Turtle, Screen, colormode
from random import randint
bert = Turtle()

# bert.shape("arrow")

# for i in range(3):
#     bert.color("red")
#     bert.forward(80)
#     bert.right(120)

# for i in range(4):
#     bert.color("orange")
#     bert.forward(80)
#     bert.right(90)

# for i in range(5):
#     bert.color("yellow")
#     bert.forward(80)
#     bert.right(72)

# for i in range(6):
#     bert.color("green")
#     bert.forward(80)
#     bert.right(60)

# for i in range(7):
#     bert.color("blue")
#     bert.forward(80)
#     bert.right(360/7)

# for i in range(8):
#     bert.color("purple")
#     bert.forward(80)
#     bert.right(360/8)

# for i in range(9):
#     bert.color("gold")
#     bert.forward(80)
#     bert.right(360/9)

# for i in range(10):
#     bert.color("black")
#     bert.forward(80)
#     bert.right(360/10)

# num_sides = 3
# colormode(255)
# while num_sides < 10:
#     bert.color(randint(1, 255), randint(1, 255), randint(1, 255))   
#     for i in range(num_sides):
#         bert.forward(80)
#         bert.right(360/num_sides)   
#     num_sides += 1

# bert.width(5)
# bert.speed("fastest")
# for i in range(200):
#     direction = randint(1,4)
#     if direction == 1:
#         bert.color("red")
#         bert.right(90)
#     if direction == 2:
#         bert.color("blue")
#         bert.right(180)
#     if direction == 3:
#         bert.color("yellow")
#         bert.left(90)
#     if direction == 4:
#         bert.color("green")
#         bert.left(180)
#     bert.forward(25)

colormode(255)
counter = 0
bert.speed("fastest")
while counter < 360:
    bert.circle(100)
    bert.right(1)
    bert.color(randint(1, 255), randint(1, 255), randint(1, 255))
    counter += 1
    
screen = Screen()
screen.exitonclick()
