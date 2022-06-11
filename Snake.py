from turtle import Turtle

startposs = [(0, 0), (-20, 0), (-40, 0)]
moveDistance = 20

up = 90
down = 270
left = 180
right = 0
class Snake:

    def __init__(self):
        self.bodyParts = []
        self.createSnake()
        self.Head = self.bodyParts[0]

    def createSnake(self):
        for pos in startposs:
            self.addPart(pos)

    def addPart(self,pos):
        newBodyPart = Turtle (shape="square")
        newBodyPart.color ("spring green")
        newBodyPart.penup ()
        newBodyPart.goto (pos)
        self.bodyParts.append (newBodyPart)

    def addExtraPart(self):
        self.addPart(self.bodyParts[-1].position())

    def move(self):
        for i in range (len(self.bodyParts) - 1, 0, -1):
            self.bodyParts[i].goto (self.bodyParts[i - 1].pos())
        self.Head.forward (moveDistance)

    def up(self):
        if(not self.Head.heading() == down):
            self.Head.setheading(90)
    def down (self):
        if (not self.Head.heading() == up):
            self.Head.setheading (270)
    def left (self):
        if (not self.Head.heading() == right):
            self.Head.setheading (180)
    def right (self):
        if (not self.Head.heading() == left):
            self.Head.setheading(0)