# import random
# from art import logo,vs
# from game_data import data

# # print(logo)
# def guess_high_or_low(firstvalue,secondvalue,score):
#     user_guess=input("Who has more followers? Type 'A' or 'B' :")
    
#     if user_guess == 'A':
#         user_value=firstvalue
#         comp_value=secondvalue
#     elif user_guess =="B":
#         comp_value=firstvalue
#         user_value=secondvalue
        
#     if user_value['follower_count'] > comp_value['follower_count']:
#         print(f"You're right ! Current score : {score+1}")
#         return f"Compare {user_guess} : {user_value['name']} , {user_value['description']} , {user_value['country']}"
#     else:
#         print("Sorry!you lose.Your score is {score}")
#         no_game_over=False
# score=0
# no_game_over=True

# while no_game_over:
#     firstvalue=random.choice(data)
#     print(f"Compare A : {firstvalue['name']} , {firstvalue['description']} , {firstvalue['country']}")
#     data.remove(firstvalue)
#     # print(vs)
#     secondvalue=random.choice(data)
#     print(f"Compare B : {secondvalue['name']} , {secondvalue['description']} , {secondvalue['country']}")
#     # answer=guess_high_or_low(firstvalue,secondvalue,score)
#     guess_high_or_low(firstvalue,secondvalue,score)

from art import logo, vs
from game_data import data
import random

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data.
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

  # Making account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct.
  ## Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen between rounds.
#   clear()
  print(logo)
  
  # Give user feedback on their guess.
  # Score keeping.
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")

