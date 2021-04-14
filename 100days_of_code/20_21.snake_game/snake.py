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
        initialize the snake method and create a segments list
        """
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        Create a snake with starting positions

        :return: a three segments snake
        """
        for position in STARTING_POSITION:
            self.add_segment(position=position)

    def add_segment(self, position):
        """
        Create new segment and assign it to the position of user choice

        :param position: get int value of user input and assign it
        """
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 100)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        """
        Add new segment to the last of the position

        :return: add existing snake new segement to its last position
        """
        self.add_segment(self.segments[-1].position())

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
        """
        Move the snake up

        :return: Move the snake up
        """
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        """
        Move the snake down

        :return: move the snake down
        """
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        """
        Move the snake left

        :return: move the snake left
        """
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        """
        Move the snake right

        :return: move the snake right
        """
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
