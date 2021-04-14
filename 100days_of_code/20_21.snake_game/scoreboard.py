from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Century', 22, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        """
        Inheritance from turtle module, write a score on the upper of the screen
        """
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update score

        :return: updated score
        """
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """
        Increase a score and updated it on the screen

        :return: increase score
        """
        self.score += 1
        self.update_scoreboard()
