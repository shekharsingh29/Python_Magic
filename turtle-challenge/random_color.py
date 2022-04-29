import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_color = (r, g, b)

    return rgb_color

angles = [0, 90, 180, 270]

ran_path = t.Turtle()
screen = t.Screen()
ran_path.pensize(15)

for _ in range(100):
    ran_path.color(random_color())
    ran_path.forward(20)
    ran_path.setheading(random.choice(angles))


screen.exitonclick()