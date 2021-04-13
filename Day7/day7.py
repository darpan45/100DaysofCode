#HANGMAN GAME
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=["apple","banana","orange","bikaner","oesaphagus","railway"]
chosen_word=random.choice(word_list)
# print(chosen_word)
display=[]
for letter in chosen_word:
    display+="_"
print(display)

end_of_game=False
lives=6
while  not end_of_game:
    guess=input("Guess your word : ").lower()

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter

    if guess not in chosen_word:
        lives-=1
        print(stages[lives])
        if lives==0:
            print("You have run out of lives.You Lose.")
            end_of_game=True

    print(display)  
    if "_" not in display:
        end_of_game=True
        print("You Win")
        print("The word was "+("".join(display))+".")
