from turtle import Screen, Turtle, distance
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping-pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
p_ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    p_ball.move()

    # bounce off y dimension
    if p_ball.ycor() >= 300 or p_ball.ycor()<= -300:
        p_ball.bounce_y()

    # bounce off x dimension after hitting paddle
    if p_ball.xcor() >= 340 and p_ball.distance(r_paddle)<=50 or p_ball.xcor() <= -340 and p_ball.distance(l_paddle)<=50 :
        p_ball.bounce_x()

    # reset ball position after histting x_cor
    if p_ball.xcor() > 380:
        p_ball.reset_position()
        score.l_score += 1
        score.score_position()

    if p_ball.xcor() < -380:
        p_ball.reset_position()
        score.r_score += 1
        score.score_position()

 
screen.exitonclick()

