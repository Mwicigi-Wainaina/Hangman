print("Welcome to Shiggy's Hangman Game!")
import random
from replit import clear
words = ["otilo", "boobies", "niggas", "thots", "tricks", "bitches", "wylin", "kristal", "henny"]
chosen_word=random.choice(words)
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
    print ("You lose bitch")
  else:
    lives=lives