from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.heads.distance(food) < 17:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.heads.xcor() > 285 or snake.heads.xcor() < -285 or snake.heads.ycor() > 285 or snake.heads.ycor() < -285:
        score.reset_game()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.heads.distance(segment) < 10:
            score.reset_game()
            snake.reset()

screen.exitonclick()
