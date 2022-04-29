from turtle import Turtle, Screen

tom_the_turtle = Turtle()
screen = Screen()

tom_the_turtle.penup()
tom_the_turtle.goto(-400,0)
tom_the_turtle.pendown()
for _ in range(0,40):
    tom_the_turtle.forward(10)
    tom_the_turtle.penup()
    tom_the_turtle.forward(10)
    tom_the_turtle.pendown()


screen.exitonclick()