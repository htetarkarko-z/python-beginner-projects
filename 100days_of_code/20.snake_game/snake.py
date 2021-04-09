from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """
        initailize the snake method and create a segemnts list
        """
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        show the snake on screen

        :return: create a turtle and turn into snake on screen
        """
        for postion in STARTING_POSITION:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(postion)
            self.segments.append(segment)
            
    def move(self):
        """
        Move the snake

        :return: move the snake at 20 pace
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cordinate = self.segments[seg_num - 1].xcor()
            y_cordinate = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cordinate, y_cordinate)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


