from turtle import Turtle

ALIGNMENT = "center"
FONT = ("JetBrains Mono", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_high") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data_high", 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


