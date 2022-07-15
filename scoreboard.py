from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-200, 230)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def level_refresh(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER !",align="center",font=FONT)

