import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_color = (r, g, b)

    return rgb_color

spiro = t.Turtle()
screen = t.Screen()

angle = 5

for _ in range(0,int(360/angle)):
    spiro.color(random_color())
    spiro.circle(100)
    spiro.setheading(spiro.heading()+5)


screen.exitonclick()