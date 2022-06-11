from turtle import Screen
import time
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update ()
    time.sleep(.1)
    snake.move()
    if(snake.Head.distance(food)<15):
        food.setLoc()
        snake.addExtraPart()
        scoreboard.increaseScore()

    if(snake.Head.xcor()>280 or snake.Head.xcor() < -280 or snake.Head.ycor() > 280 or snake.Head.ycor() < -280):
        game_is_on = False
        scoreboard.gameOver()

    for part in snake.bodyParts[1:]:
        if(snake.Head.distance(part)<10):
            game_is_on = False
            scoreboard.gameOver()


screen.exitonclick()