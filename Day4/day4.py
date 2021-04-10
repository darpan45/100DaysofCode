# import random
# import my_module
# from my_module import pi

# random_integer=random.randint(1,10)
# print(random_integer)

#returns value between 0.00000... to 0.999999999.....
# import random
# random_float= random.random()
# print(random_float)
# #if we want random decimal number between 0-5 ,then multiply the number 
# print(random_float*5)

# print(pi)
# print(my_module.pi)


#COIN TOSS
# import random
# user_choice=input("Enter your choice : heads or tails \n")
# coin_toss=random.randint(0,1)
# # if user_inp == "Heads" or user_inp =="Heads".lower():
# if coin_toss == 0:
#     coin_toss="heads"
# elif coin_toss==1:
#     coin_toss="tails"

# if user_choice == coin_toss :
#     print(f"Its {coin_toss}.You have won the toss.")
# else:
#     print(f"Its {coin_toss}.You have lost the toss.")


#UNDERSTANDING LISTS
# indian_states=["Maharashtra","Goa","Sikkim","Rajasthan","Tamilnadu"]
# print(indian_states[0])
# print(indian_states[1])
# print(indian_states[-1])
# print(indian_states[-2])

# indian_states.append("Odissa")
# indian_states.extend(["Punjab","Uttar Pradesh"])
# print(indian_states)


#BANKER ROULETTE
# import random
# names=["Darpan","Chinmay","Harsh","Amey","Pavan","Omkar"]
# print("Let's Play Banker's Roulette to see who pays the Bill.")
# bill=random.randint(0,len(names)-1)
# print(f"Today's Bill will be paid by {names[bill]}.")


## Treasure Map
# You are going to write a program which will mark a spot with an X.
# Solution
# row1=['⬜️', '⬜️', '⬜️']
# row2=['⬜️', '⬜️', '⬜️']
# row3=['⬜️', '⬜️', '⬜️']

# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}\n")

# position=input("Where do you want to put the treasure?")
#eg 32
# horizontal=int(position[0])
# vertical=int(position[1])

# map[vertical-1][horizontal-1]="X"

# print(f"{row1}\n{row2}\n{row3}\n")


##ROCK,PAPER, SCISSORS
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
# choices=["rock","paper","scissor"]
# user_choice=int(input("What do you choose ? Type 0 for Rock ,1 for Paper or 2 for Scissors "))
# comp_choice=random.randint(0,2)
# if user_choice == 0:
#     print(f"My choice : {choices[user_choice]}")
#     print(game_images[user_choice])
#     print(f"Computer choice : {choices[comp_choice]}")
#     print(game_images[comp_choice])
#     if comp_choice == 2:
#         print("Amazing! You Win.")
#     elif comp_choice ==1:
#         print("You Lose.")
#     else:
#         print("It\'s a draw.")
# elif user_choice == 1:
#     print(f"My choice : {choices[user_choice]}")
#     print(game_images[user_choice])
#     print(f"Computer choice : {choices[comp_choice]}")
#     print(game_images[comp_choice])
#     if comp_choice == 2:
#         print("You Lose.")
#     elif comp_choice ==1:
#         print("It\'s a draw.")
#     else:
#         print("Amazing! You Win.")
# elif user_choice == 2:#r,p,s
#     print(f"My choice : {choices[user_choice]}")
#     print(game_images[user_choice])
#     print(f"Computer choice : {choices[comp_choice]}")
#     print(game_images[comp_choice])
#     if comp_choice == 2:
#         print("It\'s a draw.")
#     elif comp_choice ==1:
#         print("Amazing! You Win.")
#     else:
#         print("You Lose.")
# else:
#     print("You have entered Wrong input.")

# print("CONGRATULATIONS DAY4 COMPLETE!!!!!!!!!!!")



