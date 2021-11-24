import random

# ASCII art to print whenever the player guesses wrong
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

# List of words that the computer takes a random word from for the game
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# storing the length of the word for future use

word_length = len(chosen_word)

lives = 6
# printing the word for debugging while the code is unfinished
print(chosen_word)

# Prints the empty word that you guess the letters of
display = []
display_length = 0
while display_length < word_length:
    display.append("_")
    display_length += 1
print(display)

# The game loop
# Checks to see if there is a blank character left
for character in range(len(display)):
    while display[character] == "_":
        #Player guess
        guess = input("Guess a letter: ").lower()
        if guess not in chosen_word :
            lives -= 1
            print(stages[lives])
            if lives == 0:
                break
        
        #Replace empty slot with correct guess    
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                
        #Prints the current word after correct
        print(display)
        # Checks if there are still blank spaces, if not then player wins
        if '_' not in display:
            print("You win !")
            break
    #Lose condition, no more lives
    if lives == 0:
        print("You lose!")
        break
        

