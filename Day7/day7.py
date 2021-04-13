#HANGMAN GAME
import random
from hangman_words import word_list
from hangman_art import stages,logo

# word_list=["apple","banana","orange","bikaner","oesaphagus","railway"]
chosen_word=random.choice(word_list)
print(logo)
display=[]
for letter in chosen_word:
    display+="_"
print(display)

end_of_game=False
lives=6
while  not end_of_game:
    guess=input("Guess your word : ").lower()
    if guess in display:
        print(f"You have already guessed the letter '{guess}'.Try different letter.")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life.")
        lives-=1
        print(stages[lives])
        if lives==0:
            print("You have run out of lives.You Lose.")
            print("The word was "+chosen_word+".")
            end_of_game=True

    print(display)  
    if "_" not in display:
        end_of_game=True
        print("You Win")
        print("The word was "+chosen_word+".")
        
