from turtle import Turtle

FONT = ("Courier", 50, "bold")
WIN_FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.display_score()

    def increase_right_score(self):
        self.right_score += 1
        self.display_score()

    def display_winner(self, winner):
        self.goto(0, 0)
        self.color("cyan")
        self.write(f"{winner} Player Wins! 🏅", align="center", font=WIN_FONT)
