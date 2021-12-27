import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

GAME_ON = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while GAME_ON:
    screen.update()
    time.sleep(0.05)
    snake.movement()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        GAME_ON = False
        scoreboard.game_over()

    #Detect collision with tail
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
