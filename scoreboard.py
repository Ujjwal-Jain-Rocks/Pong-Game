from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.draw()

    def draw(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_point}", align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_point}", align="center", font=("Arial", 40, "normal"))

    def update_l(self):
        self.l_point += 1
        self.draw()

    def update_r(self):
        self.r_point += 1
        self.draw()
