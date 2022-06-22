
import random

player_card = []
player_score = 0
dealer_card = []
dealer_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
acePlayer = False
aceDealer = False

def get_score(card_list):
  score = 0
  for card in card_list:
    score += card
  return score
    

def player_init():
  global player_score 
  global acePlayer
  global player_card
  randomInt = random.randint(0, len(cards)-1)
  player_card.append(cards[randomInt]) 
  #Ace check
  if cards[randomInt] == 11:
    acePlayer = True
  randomInt = random.randint(0, len(cards)-1)
  if cards[randomInt] == 11:
    acePlayer = True
  player_card.append(cards[randomInt]) 
  player_score = get_score(player_card)

def dealer_init():
  global dealer_score
  global aceDealer
  global dealer_card
  randomInt = random.randint(0, len(cards)-1)
  dealer_card.append(cards[randomInt]) 
  #Ace check
  if cards[randomInt] == 11:
    aceDealer = True
  randomInt = random.randint(0, len(cards)-1)
  if cards[randomInt] == 11:
    aceDealer = True
  dealer_card.append(cards[randomInt]) 
  dealer_score = get_score(dealer_card)
  


  
def get_additional_card(card_list, ace):
  randomInt = random.randint(0, len(cards)-1)
  card_list.append(cards[randomInt]) 
  if cards[randomInt] == 11:
    ace = True
  return 


def get_winner(player_score, dealer_score):

  if player_score > dealer_score:
    print("\nYou Win")
  elif player_score < dealer_score:
    print("\nYou loose")
  else:
    print("\nDraw")

def check_dealer(dealer_score, dealer_card):
  if dealer_score < 15:
    get_additional_card(dealer_card, aceDealer)
    get_score(dealer_card)
    return dealer_score
  else:
    return dealer_score
    

def show_result():
  print("The result is:")
  print(f"Your final hand:{player_card}, your final score   {player_score}")
  print(f"Computers final hand: {dealer_card}, computer final score {dealer_score}")
  
  get_winner(player_score, dealer_score)

def show_current_status():
  print(f"Your cards:{player_card}, your current score   {player_score}")
  print(f"Computers first card: {dealer_card[0]}")

def check_ace(score, ace):
  if score > 21 and ace == True:
    return -10
  else:
    return 0
  
def start():
  global dealer_score
  global aceDealer
  global dealer_card
  global player_score 
  global acePlayer
  global player_card
  print(player_score)
  print(f"Your cards:{player_card}, your current score   {player_score}")
  print(f"Computers first card: {dealer_card[0]}")
  another_card = input("Type 'y' to get another card, type 'n to pass' ")
 
  while another_card == "y":
      get_additional_card(player_card, acePlayer)
      player_score = get_score(player_card)
      player_score += check_ace(player_score, acePlayer)
      if player_score > 21:
        
        show_current_status()
        print("\nYou lost")
        return
        
      
      show_current_status()
      another_card = input("Type 'y' to get another card, type 'n to pass' ")
        
  else:
        dealer_score = check_dealer(dealer_score, dealer_card)
        dealer_score += check_ace(dealer_score, aceDealer)
        show_result()
        
    
  


  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play = input("Do you want to play a game of blackjack? Type 'y' or 'n'")

if play == "y":
  player_init()
  dealer_init()  
  start()
 
  



















##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

