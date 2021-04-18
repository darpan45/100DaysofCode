#Global and Local scope
#Global Variable
# apples=12
# def add_apple():
#     #local variable
#     apples=13
#     print(apples)

# add_apple()
# print(apples)

# There is no Block scope in Python (while,for,if) 

#Modifying Global Scope
# apples=12
# def add_apple():
#     global apples
#     apples+=1
#     print(apples)

# add_apple()
# print(apples)

# apples=12
# def add_apple():
#     # print(apples)
#     return apples+1

# apples=add_apple()
# print(apples)

#GUESS THE NUMBER GAME
import random
print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 to 100 ")

def guess_the_number(attempts):
    print(f"You have {attempts} attempts remaining to guess the number ")
    for i in range(attempts):
        guess=int(input("Make a guess : "))
        if guess == number:
            print("Congrats!! You have guessed the number correctly 🏆🏆")
        elif guess > number:
            print("Choose a smaller number")
        elif guess< number:
            print("Choose a greater number")
    if guess !=number:
        print("You Lose .You have run out of your lives .")
    print(f"The number was {number}.")

difficulty=input("Choose a difficulty. Type 'easy' or 'hard' : ")
number=random.randint(1,101)
attempts=0
if difficulty == "easy":
    guess_the_number(8)
elif difficulty == "hard":
    guess_the_number(5)

