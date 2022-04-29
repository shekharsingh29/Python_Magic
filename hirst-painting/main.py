import turtle as t
import extcolors, random

t.colormode(255)
colors, pixel_count = extcolors.extract_from_path('image.jpg')
color_list = []

for color in colors:
    color_list.append(color[0])
    
hirst = t.Turtle()
screen = t.Screen()

hirst.penup()
hirst.hideturtle()
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)

for row in range(0,10):
    for coloumn in range(0,10):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(40)

    hirst.setheading(90)
    hirst.forward(40)
    hirst.setheading(180)
    hirst.forward(400)
    hirst.setheading(0)

screen.exitonclick()



