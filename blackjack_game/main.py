############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

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

import random
import os
clear = lambda: os.system('clear')
from art import logo
#表示卡片數值1~13 "A"先用11表示
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_dict = {
  "A" : 11,
  "2" : 2,
  "3" : 3,
  "4" : 4,
  "5" : 5,
  "6" : 6,
  "7" : 7,
  "8" : 8,
  "9" : 9,
  "10": 10,
  "J" : 10,
  "Q" : 10,
  "K" : 10
}
user_cards = []
computer_cards = []

def get_card(gamer):
  """該gamer獲得新卡片"""
  gamer.append(random.choice(list(cards_dict.keys())))

def check_game_end():
  """檢查是否已完成遊戲結束條件"""
  #blackjack
  if get_cards_values(computer_cards) == 21 and len(computer_cards) == 2:
    print("Computer Win!! Blackjack!!!!")
    return True
  elif get_cards_values(user_cards) == 21 and len(user_cards) == 2:
    print("You Win!! Blackjack!!!!")
    return True
    
  #超過21點就爆了
  if get_cards_values(user_cards) > 21:
    print("Your score goes over 21, You Lose. QQ")
    return True
    
  if len(user_cards) == 5:
    print("Your have more than 5 cards!!! You Win!!!!")
    return True
    
  return False

def get_cards_values(gamer_cards):
    """計算該gamer目前總點數"""
    points = 0
    check_A = False
    for card_point in gamer_cards:
        point = cards_dict[card_point]
        points += point
        if point == 11:
            check_A = True
    #如果已經爆了，如有"A"調整為1並重新計算
    if points > 21 and check_A == True:
        points = 0
        for card_point in gamer_cards:
            point = cards_dict[card_point]
            if point == 11:
                point = 1
            points += point

    return points

def computer_end_game():
  """遊戲結束前，電腦繼續抽牌直到分數大於16"""
  while get_cards_values(computer_cards) < 16:
    get_card(computer_cards)

def blackjack_game():
  game_is_finished = False
  #game start
  while not game_is_finished:
    print(logo)
    user_cards = []
    computer_cards = []
    #both get 2 card
    for _ in range(2):
      get_card(user_cards)
      get_card(computer_cards)
    #顯示手牌與電腦第一張牌
    print(f"Your cards are {user_cards}")
    print(f"computer first card is {computer_cards[0]}")
  
    #確認user是否繼續要下一張卡，否則結束遊戲
    next_card = True
    #如檢查到遊戲結束，不再要卡
    if check_game_end() == True:
      next_card == False
    while next_card :
      if input("Do you want to get next card? Type 'y' or 'n' to continue.\n").lower() == 'y':          
        get_card(user_cards)
        #表示玩家要牌後爆了，直接結束遊戲
        if check_game_end() == True:
          next_card = False
        print(f"Your cards are {user_cards}")
      else:
        computer_end_game()
        next_card = False
        
    #開始顯示與比較分數
    user_final_hand = ""
    computer_final_hand = ""
    for card_type in user_cards:
      user_final_hand += card_type + ', '
    for card_type in computer_cards:
      computer_final_hand += card_type + ', '
    user_score = get_cards_values(user_cards)
    computer_score = get_cards_values(computer_cards)
    print(f"\nYour final hand {user_final_hand},and scores is {user_score}. ")
    print(f"Computer final hand {computer_final_hand},and scores is {computer_score}. ")
    
    if computer_score > 21 and user_score < 21:
      print("User Win!!!!")
    elif user_score > computer_score and user_score < 21:
      print("User Win!!!!")
    elif user_score == computer_score:
      print("Drew~~~~")
    elif computer_score > user_score and computer_score < 21:
      print("Computer Win. QQ")
  
    #如為'n'結束遊戲
    if input("\nDo you want to play again? ").lower() == 'n':
      game_is_finished = True
    clear()
blackjack_game()