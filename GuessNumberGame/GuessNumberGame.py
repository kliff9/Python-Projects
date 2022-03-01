from GuessNumberGameArt import logo
print(logo)
print('Welcome To the Number Guessing Gam\n')
print("I'm thinking of a number between 1 and 100.")

import random
num = random.randint(1, 100)
easy_attempts = 12
hard_attempts = 6


#Checks the answer and updates accordinly
def check_answer(guess, num, turns):
  if num + 3 > guess > num -3 and guess != num :
    print('Really Close')
    return turns -1
  elif guess < num:
    print('Too Low')
    return turns -1
  elif guess > num:
    print('Too High')
    return turns -1
  else:
    print(f' You Got the number right it was {num}')
    
#Sets difficulty and sets the number of attempts based on the difficulty
def difficulty():
  level= input('Choose the difficulty, Type "easy" or "hard"\n')
  if level == 'easy':
    return easy_attempts
  else:
    return hard_attempts

turns = difficulty()

#The Player keeps Guessing until They Win or Lose
while True:
  print(f"You have {turns} attempts remaining to guess the number.")
  guess = int(input('Make a Guess\n'))
  turns = check_answer(guess, num, turns)
  if turns == 0:
    print(f'You Run out of Lives You Lost, The Number was {num}')
    break
  elif guess == num:
    break
  