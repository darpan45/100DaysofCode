##Basic If Else Statement
# print("Welcome to RollerCoaster!")
# height=int(input("What is your height ? "))
# if height >= 120 :
#     print("You are eligible for rollercoaster")
# else:
#     print("You are not eligible for rollercoaster")


##Odd or Even Number
# num=int(input("Enter a number : "))
# if num % 2==0:
#     print("Number is even.")
# else:
#     print("Number is odd.")


##Nested If Else
# print("Welcome to RollerCoaster!")
# height=int(input("What is your height ? "))
# if height >= 120 :
#     print("You are eligible for rollercoaster")
#     age=int(input("What is your age ? "))
#     if age >18:
#         print("You need to pay 12$")
#     elif age >12 and age <18 :
#         print("You need to pay 7$")
#     else:
#         print("You need to pay 5$")
# else:
#     print("You are not eligible for rollercoaster")

#BMI Calculator 2.0
# weight=float(input("Enter your weight in kgs : "))
# height=float(input("Enter your height in m : "))
# bmi=weight/height**2
# bmi_round =float("{:.2f}".format(bmi))
# print(bmi_round)
# if bmi_round < 18.5:
#     print("You are underweight.")
# elif bmi_round >=18.5 and bmi_round <25:
#     print("You have normal weight.")
# elif bmi_round >=25 and bmi_round <30:
#     print("You are overweight.")
# elif bmi_round >=30 and bmi_round <35:
#     print("You are obese.")
# elif bmi_round >= 35:
#     print("You are clinically obese.")

#Leap year or not
# year =int(input("Enter a year : "))
# if year %4 ==0 :
#     if year % 400 !=0 and year %100 ==0:
#         print(f"{year} is not a leap year ")
#     else:
#         print(f"{year} is a leap year ")
# else:
#         print(f"{year} is not a leap year ")

#PIZZA ORDER 
# print("Welcome to Python Pizza Deliveries!!")
# size=input("What size pizza do you want ? S, M or L ")
# add_pepperoni = input("Do you want pepperoni ? Y or N ")
# extra_cheese=input("Do you want extra cheese ? Y or N ")

# bill=0
# if size == "S" :
#     bill +=15
#     if add_pepperoni == "Y" :
#         bill +=2
#     if extra_cheese == "Y":
#         bill +=1
# elif size == "M" :
#     bill +=20
#     if add_pepperoni == "Y" :
#         bill +=3
#     if extra_cheese == "Y":
#         bill +=1
# elif size == "L" :
#     bill +=25
#     if add_pepperoni == "Y" :
#         bill +=3
#     if extra_cheese == "Y":
#         bill +=1

# print(f"Total bill is {bill} .")

##LOVE CALCULATOR
# print("Welcome to Love Calculator!")
# name1=(input("Enter your name : "))
# name2=(input("Enter their name : "))
# lower_name1=name1.lower()
# lower_name2=name2.lower()

# T=lower_name1.count('t')+lower_name2.count('t')
# R=lower_name1.count('r')+lower_name2.count('r')
# U=lower_name1.count('u')+lower_name2.count('u')
# E=lower_name1.count('e')+lower_name2.count('e')
# print(f"T occurs {T} times .")
# print(f"R occurs {R} times .")
# print(f"U occurs {U} times .")
# print(f"E occurs {E} times .")

# TRUE=T+R+U+E
# print(f"Total {TRUE}")

# L=lower_name1.count('l')+lower_name2.count('l')
# O=lower_name1.count('o')+lower_name2.count('o')
# V=lower_name1.count('v')+lower_name2.count('v')
# E=lower_name1.count('e')+lower_name2.count('e')
# print(f"L occurs {L} times .")
# print(f"O occurs {O} times .")
# print(f"V occurs {V} times .")
# print(f"E occurs {E} times .")

# LOVE=L+O+V+E
# print(f"Total {LOVE}")
# score=str(TRUE)+str(LOVE)
# scr=int(score)
# # print(f"Your score is {score}")
# if scr<10 or scr>90:
#     print(f"Your score is {scr} ,you go together like coke and mentos.")
# elif scr >40 and scr <50 :
#     print(f"Your score is {scr} , you are alright together.")
# else:
#     print(f"Your score is {scr}.")


##TREASURE ISLAND GAME
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island !!")
# print("Your mission is to find the treasure.")
# direction=input("You're at a cross road.Where do you want to go. Type 'left' or 'right' ")
# if direction == 'left':
#     lake=input("You come to a lake.There is an island in the middle of lake. Type 'wait' to wait for the boat. Type 'swim' to swim across . ")
#     if lake =="wait":
#         door =input("You arrive at an island unharmed . There is a house with 3 doors. One red,one yellow and one blue.Which colour do you choose? ")
#         if door == "red":
#             print("You are burned in fire.")
#             print("GAME OVER!")
#         elif door =="blue":
#             print("You have been eaten by Beasts.")
#             print("GAME OVER!")
#         elif door=="yellow":
#             print("Amazing!! You have won the game .")
#         else:
#             print("GAME OVER!!")
#     else:
#         print("You have been attacked by trout.")
#         print("GAME OVER!")
# else:
#     print("You have fallen into hole.")
#     print("GAME OVER!")

# print("CONGRATULATIONS DAY3 COMPLETE!!!!!!!!!!!")