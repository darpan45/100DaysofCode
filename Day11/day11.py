# #BLACKJACK
# import random
# cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# user_cards=[]
# for i in range(2):
#     user_cards.append(random.choice(cards))
# print(f"Your Cards : {user_cards} ")
# computer_cards=[]
# for i in range(2):
#     computer_cards.append(random.choice(cards))
# print(f"Computer's first card  : {computer_cards[0]} ")
# total_user_score=sum(user_cards)
# total_comp_score=sum(computer_cards)
# print(total_comp_score)
# print(total_user_score)
# # ----------------------------------------------------------------------------
# def calculate_winner(total_user_score,total_comp_score):
#     if total_user_score >21:
#         print("You Lose .Computer Win")
#     elif total_comp_score >21:
#         print("Computer Loses .You Win")
#     else:
#         if total_user_score>total_comp_score:
#             print("Computer Loses .You Win")
#         else:
#             print("You Lose .Computer Win") 

# def code(total_user_score,total_comp_score):
#     another_user_card=input("Do you want to choose another card : Type 'y' for yes and 'n' for No  ")
#     if another_user_card=='y':
#         user_cards.append(random.choice(cards))
#         total_user_score=sum(user_cards)
#         if total_user_score <21:
#             # calculate_winner(total_user_score,total_comp_score)
#             code(total_user_score,total_comp_score)
#         elif total_user_score > 21:
#             print("You Lose .Computer Win") 
#     elif another_user_card=='n':
#         calculate_winner(total_user_score,total_comp_score)

# code(total_user_score,total_comp_score)

        

# if total_comp_score <=17:
#     computer_cards.append(random.choice(cards))
#     new_comp_card=computer_cards[-1]
#     total_comp_score=new_comp_card+total_comp_score
#     if total_comp_score >21:
#         print("Computer Loses .You Win")
        

from art import logo
import random

def deal_card():
    """
    Returns a random card from deck
    """
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return score calculated from the cards"""
    if sum(cards) ==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score,comp_score):
    if user_score==comp_score:
        return "Draw 😊😊"
    elif comp_score==0:
        return " Lose,Opponent has blackjack ☹ ☹"
    elif user_score==0:
        return "Win with a blackjack 🏆🏆"
    elif user_score > 21:
        return "You went Over .You lose ☹ ☹"
    elif comp_score > 21:
        return "Opponent went over . You win 🏆🏆"
    elif user_score>comp_score:
        return "You win 🏆🏆"
    else:
        return "Computer win .You lose ☹ ☹"

    if total_user_score >21:
        print("You Lose .Computer Win ☹ ☹")
    elif total_comp_score >21:
        print("Computer Loses .You Win 🏆🏆")
    else:
        if total_user_score>total_comp_score:
            print("Computer Loses .You Win 🏆🏆")
        else:
            print("You Lose .Computer Win ☹ ☹") 

def play_game():
    print(logo)
    user_cards=[] 
    comp_cards=[]
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)

        print(f"Your Cards : {user_cards} ")
        print(f"Computer's first card : {comp_cards[0]} ")
        if user_score==0 or comp_score==0 or user_score >21:
            is_game_over=True
        else:
            user_should_deal=input("Do you want to choose another card : Type 'y' for yes and 'n' for No  ")
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)

    print(f" Your final hand : {user_cards} , final score : {user_score}")
    print(f" Computer's final hand : {comp_cards} , final score : {comp_score}")
    print(compare_score(user_score,comp_score))

while(input("Do you want to play game of BlackJack ? Type 'y' for yes and 'n' for No ")=='y'):
    play_game()