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
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Display game over on the screen

        :return: display game over text
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase a score and updated it on the screen

        :return: increase score
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
