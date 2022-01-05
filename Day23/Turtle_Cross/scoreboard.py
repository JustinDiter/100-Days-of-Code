from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.pu()
        self.hideturtle()
        self.write_level()
    # Level counter in top left corner
    def write_level(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"Level: {self.level}",font=FONT)

    # writes the controls on the screen under the current level
    def write_controls(self):
        self.goto(-250,215)
        self.write("Press 'Up' to \ncross the road",font=("Courier", 12, "normal"))

    # Game Over screen
    def game_over(self):
        self.goto(0,0)
        self.color('black')
        self.write("GAME OVER",align='center', font=("Courier", 16, "normal") )
