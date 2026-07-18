from turtle import Turtle,Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

food = Food()
scoreboard = Scoreboard()
snake = Snake()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_speed=0.25
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        game_speed*=0.95
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()






screen.exitonclick()