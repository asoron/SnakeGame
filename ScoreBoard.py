from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.updateScoreBoard()
        self.hideturtle()

    def updateScoreBoard(self):
        self.write(f"Score : {self.Score}",align="center",font=("Arial",15,"normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",15,"normal"))

    def increaseScore(self):
        self.Score +=1
        self.clear()
        self.updateScoreBoard ()