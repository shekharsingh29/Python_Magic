from tkinter import CENTER
from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230,250)
        self.level +=1
        self.write(f'LEVEL {self.level}', move=True, align=CENTER, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=True, align=CENTER, font=FONT)
