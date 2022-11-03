import random
from replit import clear
from wordlist import word_library

print("Welcome to Shiggy's Hangman Game!")

chosen_word=random.choice(word_library)
underscore = "_"
display = []
word_length=(len(chosen_word))
picture = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
for position in range(word_length):
  display += underscore 
lives=6
end_of_game = False 
while not end_of_game:
  guess=input("Pick a letter ")
  clear()
  for position in range(word_length):
    letter=chosen_word[position]
    if letter==guess:
      display[position] = letter
  print (display)
  if guess not in chosen_word:
      lives-=1
      print (f"You have {lives} lives remaining")
      print (picture[6-lives])
  else:
    print (f"You have {lives} lives remaining")
    print (picture[6-lives])
  if "_" not in display:
    end_of_game = True
    print ("You win!")
  if lives==0:
    end_of_game = True
    print ("You lose!")
  else:
    lives=lives