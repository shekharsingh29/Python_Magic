from turtle import Turtle, Screen
import random

tom_the_turtle = Turtle()
screen = Screen()

color_list = ["dark magenta","dark orange","spring green","blue","yellow","indian red","peru","medium violet red"]

def draw_shapes(no_of_sides):
    tom_the_turtle.color(random.choice(color_list))
    angle = 360/no_of_sides
    for _ in range(0,no_of_sides):
        tom_the_turtle.forward(100)
        tom_the_turtle.right(angle)

for sides in range(3,11):
    draw_shapes(sides)

screen.exitonclick()