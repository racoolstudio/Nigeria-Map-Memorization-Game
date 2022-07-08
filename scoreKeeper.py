from turtle import Turtle

NUMBER_OF_STATES = 36
FONT = ('Impact', 30, 'normal')


class ScoreKeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.goto(250, 250)
        self.scores = 0
        self.total = NUMBER_OF_STATES
        self.write(f'Score\n{self.scores}/{self.total}', False, 'center', FONT)
        self.speed('fastest')

    def update_screen(self):
        self.clear()
        self.increase()
        self.write(f'Score\n{self.scores}/{self.total}', False, 'center', FONT)

    def increase(self):
        self.scores += 1
