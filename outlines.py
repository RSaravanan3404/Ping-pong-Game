from turtle import Turtle


class Outlines(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(2)
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line(60)
        self.penup()
        self.goto(-150, 0)
        self.draw_circle()
        self.goto(-400, -300)
        self.setheading(90)
        self.draw_line(60)
        self.setheading(0)
        self.draw_line(80)
        self.setheading(270)
        self.draw_line(60)
        self.setheading(180)
        self.draw_line(80)

    def draw_line(self, length):
        for i in range(length):
            if i % 2 == 0:
                self.pendown()
                self.forward(10)
            else:
                self.penup()
                self.forward(10)

    def draw_circle(self):
        for i in range(100):
            if i % 2 == 0:
                self.pendown()
                self.circle(150, 5)
            else:
                self.penup()
                self.circle(150, 5)

        