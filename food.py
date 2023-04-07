from turtle import Turtle
from random import randint as r

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.add_new()
        

    def add_new(self):
        location_x = r(-265, 265)
        location_y = r(-265, 265)
        self.goto(location_x, location_y)