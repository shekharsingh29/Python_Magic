from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed_of_car = STARTING_MOVE_DISTANCE

    def create_car(self):
        create_random = random.randint(1,7)
        if create_random == 1:
            self.new_car = Turtle()
            self.new_car.shape("square")
            self.new_car.penup()
            self.new_car.shapesize(stretch_wid=1,stretch_len=2)
            self.new_car.color(random.choice(COLORS))
            self.new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(self.new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_of_car)
    def increase_speed(self):
        self.speed_of_car += MOVE_INCREMENT


    