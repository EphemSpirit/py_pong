from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle(350, 0)
comp_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=player_paddle.move_up, key="Up")
screen.onkey(fun=player_paddle.move_down, key="Down")

screen.onkey(fun=comp_paddle.move_up, key="w")
screen.onkey(fun=comp_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle collision
    if ((ball.distance(player_paddle) < 50 or ball.distance(comp_paddle) < 50) and
            (ball.xcor() > 320 or ball.xcor() < -320)):
        ball.bounce_x()

    # out of bounds player
    if ball.xcor() > 380:
        scoreboard.comp_score()
        ball.reset_position()

    # left paddle misses
    if ball.xcor() < -380:
        scoreboard.player_score()
        ball.reset_position()






screen.exitonclick()