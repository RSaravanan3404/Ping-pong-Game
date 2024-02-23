from turtle import Turtle
FONT = ("Courier", 50, "normal")
WIN_SCORE = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score_board()

    def r_point(self):
        self.r_score += 1
        self.update_score_board()

    def is_game_over(self):
        if self.r_score == WIN_SCORE:
            self.final_message(side=1)
            return True
        elif self.l_score == WIN_SCORE:
            self.final_message(side=2)
            return True

    def final_message(self, side):
        self.goto(0, 0)
        self.write(f"Game Over! Player {side} wins.", align="center", font=("Courier", 20, "normal"))