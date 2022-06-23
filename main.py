
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
 
  



