import turtle
import pandas
import time
from scoreKeeper import ScoreKeeper

screen = turtle.Screen()
img = 'nigeria.gif'
screen.title('Nigeria States Game')
# add the image in the screen
screen.addshape(img)
# now img is added to turtle shape
turtle.shape(img)
# def get_location(x,y):
#     print(f',{x},{y}')
# screen.onclick(get_location)
states = pandas.read_csv('36_states.csv')
font = ('Helvetica', 10, 'normal')
state_list = states.state.tolist()

scoreKeeper = ScoreKeeper()
screen.tracer()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    user_input = screen.textinput('States in Nigeria', 'Name of State in Nigeria :').title()
    # check if the state exist

    for state_name in state_list:

        if state_name == user_input:
            x_value = float(states[states.state == user_input].x)
            y_value = float(states[states.state == user_input].y)
            pen.goto(x_value, y_value)
            pen.write(user_input, False, 'center', font)
            if state_name == 'Cross River':
                pen.clear()
                pen.write('Cross\nRiver', False, 'center', font)

            elif state_name == 'Akwa Ibom':
                pen.clear()
                pen.write('Akwa\nIbom', False, 'center', font)
            scoreKeeper.update_screen()
            state_list.remove(user_input)
        if user_input == 'Exit' or len(state_list) == 0:
                game_is_on = False
missed_data = pandas.DataFrame(state_list)
missed_data.to_csv('missed_state.csv')
turtle.mainloop()

