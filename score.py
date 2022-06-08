from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGN, font=FONT)



    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()
