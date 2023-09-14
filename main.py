import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(800, 600)

score = 0
data = pandas.read_csv("50_states.csv")

state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()
game_is_on = True

states_list = data["state"].tolist()
guessed_list = []
while game_is_on:
    user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="Name a state!").title()
    if user_answer == "Exit":
        print(guessed_list)
        still_to_guess = [state for state in states_list if state not in guessed_list]
        data_2 = pandas.DataFrame(still_to_guess)
        data_2.to_csv("states_left.csv")
        break
    if user_answer in states_list and user_answer not in guessed_list:
        x_cor = float(data[data.state == user_answer].x)
        y_cor = float(data[data.state == user_answer].y)
        guessed_list.append(user_answer)
        state_name.goto(x_cor, y_cor)
        state_name.write(user_answer, align="center")
        score += 1
        if score == 50:
            game_is_on = False


screen.exitonclick()
