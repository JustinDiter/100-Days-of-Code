import turtle
import pandas as pd

#turtle screen setup
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
df_list = df.values.tolist()

turt = turtle.Turtle()
turt.hideturtle()

correct_guesses = 0
correct_states = []

# User inputs the name of a state, if the name is correct, the name of the state is written on the map
# If the user exits before all 50 states are guessed, then the remaining states to learn are written to a csv file named 'states_to_learn.csv' created in the same folder
while correct_guesses < 50:
    answer_state = screen.textinput(title=f"Correct Answers ({correct_guesses}/50)", prompt="Type the name of a State:").title()
    if answer_state == "Exit":
        break
    for state in df_list:
        if state[0] == answer_state:
            correct_guesses += 1
            correct_states.append(state[0])
            x = state[1]
            y = state[2]
            turt.pu()
            turt.hideturtle()
            turt.goto(x,y)
            turt.write(f"{state[0]}", align='Center', font=('Courier', 8, 'normal'))
    
# states to learn.csv
states_to_learn = []
for state in df_list:
    if state[0] in correct_states:
        continue
    states_to_learn.append(state[0])

df_states_to_learn = pd.DataFrame(states_to_learn)

df_states_to_learn.to_csv("states_to_learn.csv")
