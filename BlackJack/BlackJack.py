############### Blackjack Project #####################


import random
from typing import List
from BlackJackArt import logo

#This Functions Returns a Random Number
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
#This Function compares the score when Both While loops are Stopped
def compare(user_score, computer_score):

  if user_score == computer_score:
    return "Draw 🙃"
  if user_score > 21 and computer_score > 21:
    return "You went over."
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"



#Function That Continues to calculates the score if there No Instant Win
def calculate_score(cards):
  if 11 in cards and 10 in cards and len(cards) == 2:
    return 0
  elif sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  else:
    return sum(cards)
#The Black Jack Game
def playGame():
  #Place Holder
  computer_cards = []
  user_cards = []
  game = False
  print(logo)
  #Appends the Randomize number to the empty List
  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    #The player May Continue to Draw Until they decide to Stop
  while not game:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f'Your Cards:{user_cards} Which sums up to {user_score}')
      print(f'Computer First Card is :{computer_cards[0]}')

      if user_score == 0 or computer_score == 0 or user_score > 21:
        game = True
      else: 
        draw= input('Type (y) to draw a card or(n) to pass\n').lower()
        if draw == 'y':
          user_cards.append(deal_card())

          
        else:
          game = True

  #When The While loop above is set to Stop, then The Computer While loop will begin  and draw cards until their score is over 17

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  


  #Final Results
  print(f'\n Your Final Hand: is {user_cards} and Score is: {user_score}')
  print(f'\n The Computer Final Hand: is {computer_cards} and Score is: {computer_score}\n')

  print(compare(user_score, computer_score))

while input('\nDo you want to play a game of BlackJack (y/n)\n') == 'y':
  playGame()


