import turtle
import pandas
import time
from scoreKeeper import ScoreKeeper

# Initialize the turtle screen and set the title
screen = turtle.Screen()
img = 'nigeria.gif'
screen.title('Nigeria States Game')

# Add the image to the screen
screen.addshape(img)

# Set the turtle shape to the loaded image
turtle.shape(img)

# Load the list of Nigerian states from the CSV file
states = pandas.read_csv('36_states.csv')

# Define the font for displaying state names
font = ('Helvetica', 10, 'normal')

# Convert the list of states to a Python list
state_list = states.state.tolist()

# Create an instance of the ScoreKeeper class to track the player's score
scoreKeeper = ScoreKeeper()

# Update the screen with the latest changes
screen.tracer()

# Set up a loop for the game
game_is_on = True
while game_is_on:
    # Add a slight delay and update the screen to ensure smooth animation
    time.sleep(0.01)
    screen.update()

    # Create a new pen for writing state names on the screen
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()

    # Prompt the user to enter the name of a state in Nigeria
    user_input = screen.textinput('States in Nigeria', 'Type EXIT to end the game \nName of State in Nigeria:').title()

    # Check if the state exists in the list
    for state_name in state_list:
        if state_name == user_input:
            # Get the coordinates for the state on the map and write the name of the state there
            x_value = float(states[states.state == user_input].x)
            y_value = float(states[states.state == user_input].y)
            pen.goto(x_value, y_value)
            pen.write(user_input, False, 'center', font)

            # Special cases for states with long names to fit them on the map properly
            if state_name == 'Cross River':
                pen.clear()
                pen.write('Cross\nRiver', False, 'center', font)
            elif state_name == 'Akwa Ibom':
                pen.clear()
                pen.write('Akwa\nIbom', False, 'center', font)

            # Update the score on the screen and remove the state from the list
            scoreKeeper.update_screen()
            state_list.remove(user_input)

        # Check if the user wants to exit the game or if all states have been correctly guessed
        if user_input == 'Exit' or len(state_list) == 0:
            game_is_on = False

# Save the list of missed states to a CSV file
missed_data = pandas.DataFrame(state_list)
missed_data.to_csv('missed_state.csv')

# Keep the turtle window open until the user closes it
turtle.mainloop()
