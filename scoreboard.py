from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.show_scoreboard()
        self.hideturtle()

    def get_highscore(self):
        with open("data.txt", 'r') as file:
            content = file.read()
            return int(content[0])


    def show_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} | High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.high_score, self.score)
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.show_scoreboard()

    def add_score(self):
        self.score += 1
        self.show_scoreboard()
