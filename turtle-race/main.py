import turtle as t
import random 

color_list = ['red','orange','yellow','green','purple','black']

screen = t.Screen()
screen.setup(600,500)

turtles = []

bet_turtle_color = t.textinput("PLACE BET", "Which color turtle will win ?")

for turtle_index in range(0,6):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-280, -220+turtle_index*85)

    turtles.append(new_turtle)

if bet_turtle_color:
    game_is_on = True

while game_is_on:
    for turtle in turtles:
        random_distance = random.randint(3,15)
        turtle.forward(random_distance)
        if turtle.xcor() > 280:
            game_is_on = False
            if turtle.pencolor() == bet_turtle_color:
                print(f'You win the bet, {turtle.pencolor()} won the race')
            else:
                print(f'You lose the bet, {turtle.pencolor()} won the race')

screen.exitonclick()