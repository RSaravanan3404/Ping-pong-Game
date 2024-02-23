from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from outlines import Outlines
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("green")

screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score = Scoreboard()
midline = Outlines()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    game_over = score.is_game_over()
    if game_over:
        ball.penup()
    if ball.ycor() > 284 or ball.ycor() < -284:
        ball.wall_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -355:
        ball.paddle_bounce()
    elif ball.xcor() > 370:
        ball.refresh()
        score.l_point()
    elif ball.xcor() < -370:
        ball.refresh()
        score.r_point()

screen.exitonclick()
