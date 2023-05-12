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

def get_card(gamer):
  """該gamer獲得新卡片"""
  gamer.append(random.choice(list(cards_dict.keys())))

def get_cards_values(gamer_cards):
    """計算該gamer目前總點數"""

    return_points = 0
    #計算總點數
    for card_point in gamer_cards:
      check_A = False
      if 'A' in card_point:
        check_A = True
      return_points += cards_dict[card_point]

    #如果已經爆了，如有"A"調整為1並重新計算
    if return_points > 21 and check_A == True:
        return_points = 0
        for card_point in gamer_cards:
            point = cards_dict[card_point]
            if card_point == "A":
                point = 1
            return_points += point

    return return_points
    
def auto_game(gamer_cards):
  """自動抽牌直到分數大於17"""
  while get_cards_values(gamer_cards) != 0 and get_cards_values(gamer_cards) < 17:
    get_card(gamer_cards)

def blackjack_game():
  #game start
  print(logo)
  user_cards = []
  computer_cards = []
  next_card = True
    
  #both get 2 card
  for _ in range(2):
    get_card(user_cards)
    #computer_cards = ['A','10']
    get_card(computer_cards)
  #顯示手牌與電腦第一張牌
  user_score = get_cards_values(user_cards)
  print(f"Your cards are {user_cards}, current score: {user_score}")
  print(f"computer first card is {computer_cards[0]} \n")

  #blackjack不再抽排，將分數以0表示，直接結束遊戲
  user_score = get_cards_values(user_cards)
  computer_score = get_cards_values(computer_cards)
  if computer_score == 21 and len(computer_cards) == 2 :
    computer_score = 0
    next_card = False
  elif user_score == 21 and len(user_cards) == 2:
    user_score = 0
    next_card = False
    
  while next_card:
    if input("Do you want to get next card? Type 'y' or 'n' to continue.\n").lower() == 'y':          
      get_card(user_cards)
      #超過21點就爆了
      if get_cards_values(user_cards) > 21:
        next_card = False
        user_score = get_cards_values(user_cards)
      else:
        user_score = get_cards_values(user_cards)
        print(f"Your cards are {user_cards}, current score: {user_score}")
    else:
      next_card = False

  #玩家結束，電腦自動抽排
  if computer_score != 0 and user_score <= 21:
    auto_game(computer_cards)
    computer_score = get_cards_values(computer_cards)
         
  #開始顯示與比較分數
  user_final_hand = ""
  computer_final_hand = ""
  for card_type in user_cards:
    user_final_hand += card_type + ', '
  for card_type in computer_cards:
    computer_final_hand += card_type + ', '
    
  print(f"\nYour final hand {user_final_hand},and scores is {user_score}. ")
  print(f"Computer final hand {computer_final_hand},and scores is {computer_score}. ")

  if computer_score == 0:
    print("Computer Win!! Blackjack!!!!")
  elif user_score == 0:
    print("You Win!! Blackjack!!!!")
  elif computer_score > 21 and user_score < 21:
    print("User Win!!!!")
  elif user_score > computer_score and user_score < 21:
    print("User Win!!!!")
  elif user_score == computer_score:
    print("Drew~~~~")
  elif computer_score > user_score and computer_score < 21:
    print("Computer Win. QQ")
  elif user_score > 21:
    print("Your score goes over 21, You Lose. QQ")
  
    
blackjack_game()
while input("\nDo you want to play again? ").lower() == 'y':
  clear()
  blackjack_game()
  