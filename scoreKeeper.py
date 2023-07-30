from turtle import Turtle

NUMBER_OF_STATES = 36
FONT = ('Impact', 30, 'normal')


class ScoreKeeper(Turtle):
    def __init__(self):
        # Initialize the ScoreKeeper as a Turtle object
        super().__init__()

        # Hide the turtle and lift the pen up
        self.hideturtle()
        self.penup()

        # Set the starting position for the score display
        self.goto(250, 250)

        # Initialize the scores and total number of states
        self.scores = 0
        self.total = NUMBER_OF_STATES

        # Write the initial score display on the screen
        self.write(f'Score\n{self.scores}/{self.total}', False, 'center', FONT)

        # Set the turtle's speed to the fastest
        self.speed('fastest')

    def update_screen(self):
        # Clear the previous score display
        self.clear()

        # Increment the scores and write the updated score display
        self.increase()
        self.write(f'Score\n{self.scores}/{self.total}', False, 'center', FONT)

    def increase(self):
        # Increment the scores by 1
        self.scores += 1
