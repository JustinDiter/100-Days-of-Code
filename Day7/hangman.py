import random
from hangman_words import word_list
from hangman_art import logo_art, stages

# Print the logo from the art file
print(logo_art)

# List of words that the computer takes a random word from for the game
chosen_word = random.choice(word_list)

# storing the length of the word for future use
word_length = len(chosen_word)

# storing the amount of lives the player has until game over
lives = 6

# printing the word for debugging while the code is unfinished
# print(f"For debugging purposses, the word is {chosen_word}.")

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

        #Player guess, making ensuring that the input is also lowercase
        guess = input("Guess a letter: ").lower()

        #checks to see if the guess is incorrect, if it is then player loses a life
        if guess not in chosen_word :
            print(f"You guessed {guess}, unfortunately that's not in the word. You lose a life.")
            lives -= 1
            print(stages[lives])
            if lives == 0:
                break
        
        if guess in display :
          print("You've already correctly guessed that. You don't lose a life.")
        
        #Replace empty slot with correct guess    
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f"You guessed {guess}, that's correct !")
                
        #Prints the current word after every turn.
        print(display)
        # Checks if there are still blank spaces, if not then player wins
        if '_' not in display:
            print("You win !")
            break
    #Lose condition, no more lives
    if lives == 0:
        print("You lose!")
        break
        

