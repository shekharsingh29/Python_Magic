from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_position()        


    def score_position(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        