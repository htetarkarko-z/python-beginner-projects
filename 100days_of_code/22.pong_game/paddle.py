from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=position[0], y=position[1])

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)