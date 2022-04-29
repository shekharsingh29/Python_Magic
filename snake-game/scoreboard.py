from turtle import Turtle
import re

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open('score.txt', mode='r') as read_score_file:
            self.content = re.split("=", read_score_file.read())
            self.highest_score = int(self.content[1])
            read_score_file.close()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} -- highest Score: {self.highest_score} ",False, align="center")

    def game_over(self):
        self.clear()
        self.goto(0,0)
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('score.txt',"w") as write_score_file:
                write_score_file.write(f'highest_score={self.highest_score}')
                write_score_file.close()
        self.write(f'GAME OVER',align='center')

