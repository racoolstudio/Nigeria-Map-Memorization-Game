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


def endgame(stateList):
    # Function to handle end of the game and display the missed states
    # Create a turtle to display the message about missed states in a box
    missing_text = turtle.Turtle()
    missing_text.hideturtle()
    missing_text.penup()
    missing_text.goto(-210, 250)

    if len(stateList) > 0:
        # If there are missed states, display them in red and their names on the map
        missing_text.color('red')
        missing_text.write('The State(s) You Missed Is/Are in Red', False, 'center', 20)

        for missing_state_name in stateList:
            pen.color('red')
            pen.goto(float(states[states.state == missing_state_name].x),
                     float(states[states.state == missing_state_name].y))
            # Special cases for states with long names to fit them on the map properly
            if missing_state_name == 'Cross River':
                pen.write('Cross\nRiver', False, 'center', font)
            elif missing_state_name == 'Akwa Ibom':
                pen.write('Akwa\nIbom', False, 'center', font)
            else:
                pen.write(missing_state_name, False, 'center', font)
    else:
        # If all states are correctly guessed, display a message in green
        missing_text.color('Green')
        missing_text.write('You did it !!! Nigeria Blood Flows In You 🫡🇳🇬', False, 'center', 40)

    # Save the list of missed states to a CSV file
    missed_data = pandas.DataFrame(state_list)
    missed_data.to_csv('missed_state.csv')


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
    try:
        user_input = screen.textinput('States in Nigeria',
                                      'Type EXIT to end the game \nName of State in Nigeria:').title()
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
            if user_input == 'Exit' or len(state_list) == 0 or user_input is None:
                game_is_on = False
                endgame(state_list)
    except AttributeError:
        # Handle AttributeError (e.g., when the user clicks the 'Cancel' button in the input dialog)
        game_is_on = False
        endgame(state_list)

# Keep the turtle window open until the user closes it
turtle.mainloop()
