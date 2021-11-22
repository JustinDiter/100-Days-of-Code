import random

# ASCII art to display during game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Where the choices are stored

player_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

computer_choice = random.randint(0,2)

# Deciding which ASCII art to display

if player_choice == 0 :
    print(rock)
elif player_choice ==1 :
    print(paper)
elif player_choice == 2 :
    print(scissors) 
else :
    print("Invalid input, I will pick a random choice for you instead.")
    player_choice = random.randint(0,2)
    if player_choice == 0 :
        print(rock)
    elif player_choice ==1 :
        print(paper)
    elif player_choice == 2 :
        print(scissors)

print("Computer Chose:")

if computer_choice == 0 :
    print(rock)
elif computer_choice ==1 :
    print(paper)
elif computer_choice == 2 :
    print(scissors) 

# Game logic
loss = "You lose."
win = "You win !"
# Draw

if player_choice == computer_choice :
    print("It's a draw !")

# Player picks Rock

if player_choice == 0 and computer_choice == 1 :
    print(loss)
elif player_choice == 0 and computer_choice == 2 :
    print(win)

# Player picks Paper

if player_choice == 1 and computer_choice == 2 :
    print(loss)
elif player_choice == 1 and computer_choice == 0 :
    print(win)

# Player picks Scissors

if player_choice == 2 and computer_choice == 0 :
    print(loss)
elif player_choice == 2 and computer_choice == 1 :
    print(win)

