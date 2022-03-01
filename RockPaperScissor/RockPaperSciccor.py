while True:
 rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

 paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

 scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Players Chooses their choice
 inp = int(input('rock(1), paper(2) or sissor(0)\n'))


# Computer Rnadmoized Choices

 import random
 slot = random.randint(0,2)                    #
 if slot == 0:
  print('Computer:')
  print(scissors)
 elif slot == 1:
  print('Computer:')
  print(rock)
 elif slot == 2:
   print('Computer:')
   print(paper)

# User Input Choices

 if inp == 0:
  print('You:')
  print(scissors)
 elif inp == 1:
  print('You:') 
  print(rock)
 elif inp == 2:
  print('You:') 
  print(paper)

 #Variables for the Game Wins
 player = 'You Win!'
 computer = 'Computer Wins!'


# Rules Enformance With Message
 if inp == 0 and slot == 1:
  print(computer)
 elif inp == 1 and slot == 2:
  print(computer)

 elif inp == 2 and slot == 0:
  print(computer)

 elif inp == 1 and slot == 0:
  print(player)

 elif inp == 2 and slot == 1:
  print(player)

 elif inp == 0 and slot == 2:
  print(player)

 elif inp == slot:
  print('Its A TIE!')
 else: #Player option to continue or Stop the game
  print("You typed an invalid number, you lose!") 
 play_again= input('Would you like to play Again? Yes(y) No(n)\n')
 if play_again == 'n':
   break


#computer draw
# x = random.randint(0,2)

# def roll (x):
   
#    if x == 0:
#       print('Papper')
#    elif x == 1:
#       print('Rock')
#    elif x == 2:
#       print('Scissors') 

# y = int(input('Number'))
# def Results (y):
#    if x == 0 and y == 1