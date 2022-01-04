from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Screen window config
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

# Positioning Paddles
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))

# Player controls
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "z")
screen.onkeypress(paddle_l.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

# Game loop flag
game_is_on = True

while game_is_on:

    # Game fluidity/speed
    time.sleep(0.02)
    screen.update()
    screen.listen()
    
    ball.move()
    
    # Collision Detection with Walls, ball speed increases
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_walls()

    # Collision Detection with Right Paddle, ball speed increases 
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50:
        ball.setx(320)
        ball.bounce_paddle()
        ball.x_move -= 1

    # Collision Detection with Left Paddle
    if ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.setx(-320)
        ball.bounce_paddle()
        ball.x_move += 1

    # Right misses, Left scores
    if ball.xcor() > 410: 
        ball.reset_ball()
        scoreboard.l_scores()
        ball.x_move = 7
        

    # Left misses, Right scores
    if ball.xcor() < -410:
        ball.reset_ball()
        scoreboard.r_scores()
        ball.x_move = 7
        

screen.exitonclick()
