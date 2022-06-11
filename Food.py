from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5)
        self.color("red")
        self.speed("fastest")
        self.setLoc()


    def setLoc(self):
        self.goto ((random.randint (0, 13) * 20, random.randint (0, 13) * 20))