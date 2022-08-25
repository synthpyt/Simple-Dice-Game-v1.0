# /// creating a simple dice program ///
# 1 - importing important modules
from replit import clear
import random
# 2 - Greet the user
def greet():
  print("Hello and welcome to DiceRoller!")

greet()
# 3 -  Start the main the program
game_end = False
dice = random.randint(1, 6)
roll_or_not = input("Do you want to roll the Dice? 'y' or 'n'\n")
if roll_or_not == 'n' or roll_or_not == "no":
  game_end = True
  print("Goodbye!")
while not game_end:
  print("The Dice is Rolling...")
  print(f"The dice landed on {dice}!")
  roll_again = input("Do you wanna roll the dice again?\n")
  if roll_again == 'no' or roll_again == 'n':
    game_end = True
    print("Goodbye!")
  elif roll_again == 'y' or roll_again == 'yes':
    dice2 = random.randint(1, 6)
    print(f"Your Dice landed on {dice2}!")
    game_end = False
    
  
  
  
  
