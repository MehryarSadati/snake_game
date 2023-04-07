from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def compute_sleep_interval(level):
    if level.lower() == "hard":
        return 0.05
    if level.lower() == "medium":
        return 0.1
    return 0.15


def has_snake_eaten_food(snake, food):
    return snake.head.distance(food) < 20


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Snack")
screen.tracer(0)
level = screen.textinput("LEVEL", "please chose a level:\n(easy/medium/hard)")

sleep_interval = compute_sleep_interval(level)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(sleep_interval)
    snake.move()

    if has_snake_eaten_food(snake, food):
        food.add_new()
        score_board.refresh()
        snake.extend()

    if snake.game_over():
        is_game_on = False
        score_board.show_game_over()


screen.exitonclick()
