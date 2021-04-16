import turtle
import pandas

# set screen size, title and background
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title('Guess the US State')
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# read csv file and store state data in a list
data_file = pandas.read_csv('./50_states.csv')
states = data_file.state.to_list()

# declare list and an integer for guessed state and score
guessed_state = []
score = 0

# main game loop valid until all state are correct
while len(guessed_state) < 50:
    # show user score and get input for state and exit
    user_guess = screen.textinput(title=f'{len(guessed_state)}/ 50 State Correct',
                                  prompt='Enter Your Name').capitalize()
    # if user exit return missing state
    if user_guess == 'Exit':
        missing_state = pandas.DataFrame([state for state in states if state not in guessed_state])
        missing_state.to_csv('state_to_learn.csv')
        break
    # if user guess is already guessed then pass
    elif user_guess in guessed_state:
        pass
    # if user guess is in state, return state name on map and track score and append state name
    elif user_guess in states:
        guessed_state.append(user_guess)
        score += 1
        coordinate = data_file[data_file['state'] == user_guess]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(coordinate.x), int(coordinate.y))
        t.write(user_guess)
