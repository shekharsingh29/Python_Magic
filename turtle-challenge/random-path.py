from turtle import Turtle, Screen
import random

color_list = ["dark magenta","dark orange","spring green","blue","yellow","indian red","peru","medium violet red"]
angles = [0, 90, 180, 270]

ran_path = Turtle()
screen = Screen()
ran_path.pensize(15)

for _ in range(100):
    ran_path.color(random.choice(color_list))
    ran_path.forward(20)
    ran_path.setheading(random.choice(angles))


screen.exitonclick()