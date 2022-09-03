import random
import turtle

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet !", prompt="Which turtle will win the race ?Enter color: ")
colors = ["red", "blue", "black", "green", "orange", "pink", "cyan"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
turtle_list = []

for _ in range(7):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[_])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            win = turtle.pencolor()
            is_race_on = False
            if user_bet == win:
                print(f"You won ! The {win} turtle is the winner.")
            else:
                print(f"You lose ! The {win} turtle is the winner.")
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
