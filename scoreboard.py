from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.write('Score: {}'.format(self.score), align='center', font=('Courier', 24, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.write('Score: {}'.format(self.score), align='center', font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 24, 'normal'))
