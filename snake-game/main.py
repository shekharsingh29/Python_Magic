from turtle import Turtle, Screen
import time
from snake import Snake
from food import turtleFood
from scoreboard import scoreBoard

screen = Screen()
screen.setup(600, 600)

screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
snake_food = turtleFood()
game_score = scoreBoard()
game_is_on = True


screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        game_score.game_over()
    elif snake.head.distance(snake_food) < 15:
        snake_food.refresh_move()
        game_score.score +=1
        game_score.refresh_score()
        snake.extend_snake(snake.segments[-1].position())

screen.exitonclick()