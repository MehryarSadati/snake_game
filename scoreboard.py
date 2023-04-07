from turtle import Turtle
import time

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 50, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def show_game_over(self):
        self.goto(0, 0)
        for _ in range(5):
            self.write("GAME OVER!", align=ALIGNMENT, font=GAME_OVER_FONT)
            self.color("black")
            time.sleep(0.2)
            self.write("GAME OVER!", align=ALIGNMENT, font=GAME_OVER_FONT)
            self.color("white")
            time.sleep(0.2)

    def refresh(self):
        self.score += 1
        self.clear()
        self.update()
