from tkinter import CENTER
import turtle as t, pandas as p


from numpy import imag

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
t.penup()

score = 0
guessed_state = []
game_is_on = True

state_data = p.read_csv("50_states.csv")
states = state_data["state"].to_list()
co_ordinates = state_data.to_dict('records') 

while game_is_on:

    guess = screen.textinput(f"{score}/50 States Correct", "What's another state name").title()

    if guess in states and guess not in guessed_state:
        guessed_state.append(guess)
        score += 1
        
        x = co_ordinates[states.index(guess)]['x']
        y = co_ordinates[states.index(guess)]['y']
        t.goto(x,y)
        t.write(guess,True,align='center')
        t.goto(0,0)
    else:
        pass   

screen.exitonclick()