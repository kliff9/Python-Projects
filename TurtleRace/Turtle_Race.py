from turtle import Turtle, Screen
import random
# --------------------------------------+Turtle Race---------------------------------------------
screen = Screen()
screen.setup(width=700, height=500) #Set the size and position of the main window. 
user_bet = screen.textinput(title='Make your bet', prompt= "which Turtle Will win the race? Enter a color") #Pop up a dialog window for input of a string
colors = ['cyan2', 'DarkOrange4', 'DeepPink1', 'blue', 'DarkSlateBlue', 'red']
y_position = [-120,-60, 0, 60, 120, 180]
all_turtles = [] # objects for the turtles

race = False # the While Trigger
for turtle in range(0, 6): #6 new "object being created"
    new = Turtle(shape='turtle')
    new.penup() # no line being drawn when moving
    new.goto(x=-330, y=-y_position[turtle]) # Tutle is 40 x 40 so we have to divide 40/2 be the width(x-cordinate) also we change the y-cor with index from a list
    new.color(colors[turtle]) #give turtle a new color based on index
    all_turtles.append(new) #each turtle new turtle is added to the list

if user_bet: # if user enters a bet
    race = True
while race:
    for turtle in all_turtles: # 1. checks if turtles hits a certain cord(finish line)
      if turtle.xcor() > 330: #2. if not then the Loop we keep randomizing .foward movements
        race = False            #3 When finish line is reach then the bet is checked and game is stooped
        win_turtle = turtle.pencolor()
        if user_bet == win_turtle:
            print(f'You have Won The winning Color was {win_turtle}')
        else:
            print(f'You have Lost The winning Color was {win_turtle}')
      rand_distance = random.randint(0,10)
      turtle.forward(rand_distance)
    


screen.exitonclick() 
