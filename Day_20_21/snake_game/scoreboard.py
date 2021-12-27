from turtle import Turtle

ALIGNMENT = "Center"
FONT = "Courier"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(x=0,y=270)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= (FONT, 18, "normal"))

    def game_over(self):
        self.pu
        self.goto(x=0,y=0)
        self.write(f"GAME OVER", align="center", font= (FONT, 26, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()