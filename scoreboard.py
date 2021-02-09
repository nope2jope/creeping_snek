from turtle import Turtle

TEXT = "Score: "
HS = "High score : "
INIT = (0, 275)
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(INIT)
        self.pencolor("white")
        self.score = 0
        with open("high_score.txt") as file:
            self.highscore = file.read()
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(TEXT + f"{self.score}" + "  " + HS + f"{self.highscore}", align=ALIGNMENT, font=FONT)

    def plus_one(self):
        self.score += 1
        self.update_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("G A M E  O V E R", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        if int(self.score) > int(self.highscore):
            self.highscore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_board()
