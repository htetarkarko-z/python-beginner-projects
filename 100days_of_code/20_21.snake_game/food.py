from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        """
        Create a food instance set size, color, speed and show a random position at screen
        """
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """
        Refresh food at random position

        :return: refresh food at random position
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
