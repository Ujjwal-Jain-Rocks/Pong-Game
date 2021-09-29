import time
from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
is_game_on = True


def game_over():
    global is_game_on
    is_game_on = False


screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")
screen.onkey(game_over, "x")

while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(paddle1) < 50) or (ball.xcor() < -320 and ball.distance(paddle2) < 50):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.update_l()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.update_r()

screen.exitonclick()
