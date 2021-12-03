from higher_lower_data import data
from higher_lower_art import logo, vs
import random
import os

print(logo)
# Clear function for windows
clear = lambda: os.system('cls')

# chooses the initial A and B
choice_A = random.choice(data)
choice_A_name = choice_A['name']
choice_A_followers = choice_A['follower_count']
choice_A_description = choice_A['description']
choice_A_country = choice_A['country']

choice_B = random.choice(data)
if choice_B == choice_A:
  choice_B = random.choice(data)
choice_B_name = choice_B['name']
choice_B_followers = choice_B['follower_count']
choice_B_description = choice_B['description']
choice_B_country = choice_B['country']

def random_b():
  '''function to retrieve random choice B from data list'''
  global choice_B
  global choice_B_name
  global choice_B_followers
  global choice_B_description
  global choice_B_country
  global choice_A
  choice_B = random.choice(data)
  if choice_B == choice_A:
    choice_B = random.choice(data)
  choice_B_name = choice_B['name']
  choice_B_followers = choice_B['follower_count']
  choice_B_description = choice_B['description']
  choice_B_country = choice_B['country']


def switch_A_B():
  '''function that switches A and B for the next round when B is higher than A in the game'''
  global choice_A
  global choice_A_name
  global choice_A_followers
  global choice_A_description
  global choice_A_country
  choice_A = choice_B
  choice_A_name = choice_B['name']
  choice_A_followers = choice_B['follower_count']
  choice_A_description = choice_B['description']
  choice_A_country = choice_B['country']


def print_game():
  '''function that prints the game's graphics'''
  print(f"A: {choice_A_name}, a {choice_A_description}, from {choice_A_country}.")
  
  print(vs)
  
  print(f"B: {choice_B_name}, a {choice_B_description}, from {choice_B_country}.")

# loop flag
has_lost = False

# initialize player score
player_score = 0


def game_loop():
  '''game loop: defines correct choice, checks if player choice is correct, if it is, +1 point and game continues, wrong -> game over'''
  global has_lost
  global player_score
  correct_choice = 0
  if choice_A_followers > choice_B_followers:
    correct_choice = 'A'
  else:
    correct_choice = 'B'

  player_guess = str(input("Guess who has the most instagram followers: "))

  if player_guess == correct_choice:
    player_score += 1
    clear()
    print(f"Correct ! You gain a point. Your current score is {player_score}")
    return
  else:
    clear()
    print(f"Wrong. Your score was {player_score}")
    has_lost = True
    return

# initialize game
print_game()
print("Welcome to the higher-lower game.")
game_loop()

# if the player hasn't lost, continue the game by switching the previous correct choice to A and have B be a new random element from the data list
while not has_lost: 
  if choice_A_followers > choice_B_followers:
    random_b()
    print_game()
    game_loop()
  elif choice_B_followers > choice_A_followers:
    switch_A_B()
    random_b()
    print_game()
    game_loop()
    
