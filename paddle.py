from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.6)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
