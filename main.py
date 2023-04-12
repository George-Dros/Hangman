# Needs clear
import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)                      #Start game
input("Press any key (except space-bar) to play!")

lives = 6                  #6 Trials

current_stage = stages[lives]  # Start with the gallows only


chosen_word = random.choice(word_list) #PC-choice from word list

print(current_stage)
word_list = list(chosen_word) #make choice into a list
display = list(chosen_word)   #Display to player

for i in range(len(display)):
  display[i] = "_"            #Display should indicate "_" letters. 
print(display) 

game_ended = False

while word_list != display and game_ended == False:  #Play
  
  guess = input("Guess a letter: ").lower()
  Lose_life = True
  
  for position in range(len(chosen_word)):
    
    
    if chosen_word[position] == guess and display[position] == "_":
      display[position] = guess
      Lose_life = False
      

    elif chosen_word[position] != guess and display[position] != "_":
      display[position] = chosen_word[position]
      
      
    else:
      display[position] = "_"
      
      
  if Lose_life == True:                   #Getting hanged
    lives -=1
    current_stage = stages[lives]
    print(f"{guess} is not in the word, try again!")
    
  print(display)
  print(current_stage)

  if lives == 0:                     #Loss condition
    print("You Lost!")
    print(f"The word was: {chosen_word}")
    game_ended = True

  elif word_list == display:         #Win condition
    print("YOU WIN!")
    print(f"{chosen_word}")
    game_ended = True