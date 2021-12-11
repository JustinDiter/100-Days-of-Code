from turtle import Turtle, Screen
import random

# setting up the screen
screen = Screen()
screen.setup(width=500, height=400)

# user input to bet on which turtle to win
user_bet = screen.textinput(title="Make your bet", prompt="Guess which color turtle will win the race: ")
print(user_bet)

# race loop flag
race_is_on = False

# the differences in the turtles during initialization
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-90, -60, -30, 0, 30, 60]
turtle_racers_list = []

# creates each turtle
for turt in range(0, 6):
    turtle_racer = Turtle(shape = "turtle")
    turtle_racer.pu()
    turtle_racer.color(colors[turt])
    turtle_racer.goto(x=-230, y=y_positions[turt])
    turtle_racers_list.append(turtle_racer)

# starts the race once the user has made a bet
if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in turtle_racers_list:
        # finish line
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner !")
            else:
                print(f"Better luck next time. The {winning_color} turtle is the winner.")

        # gives each turtle a random varying speed
        random_dash = random.randint(0, 10)
        turtle.forward(random_dash)


screen.exitonclick()
