from turtle import Turtle
import random

class turtleFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.refresh_move()        



    def refresh_move(self):
        new_x = random.randint(-280,280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)