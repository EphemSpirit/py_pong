from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle(350, 0)
comp_paddle = Paddle(-350, 0)

screen.listen()

screen.onkey(fun=player_paddle.move_up, key="Up")
screen.onkey(fun=player_paddle.move_down, key="Down")

screen.onkey(fun=comp_paddle.move_up, key="w")
screen.onkey(fun=comp_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()






screen.exitonclick()