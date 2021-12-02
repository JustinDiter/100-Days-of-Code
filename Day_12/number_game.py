from number_game_art import logo
import random

print(logo)

print("Welcome to the number game !")
print("I'm thinking of a number between 1 and 100.")
print("Try to take a guess at which one it is.")
# Play again loop flag
play_again = True
while play_again:
    # player decides if they want 10 lives or 5 lives
    difficulty = input("Would you like to play on the 'easy' difficulty or 'hard' difficulty?: ")
    # generates number to guess
    game_number = random.randint(1,100)
    # flag checking if player has won, if yes, game stops and 'you win'
    has_won = False
    # game function
    def game():    
        player_guess = int(input("Make a guess: "))
        global has_won
        if player_guess > game_number:
            return print("Too high.")
        if player_guess < game_number:
            return print("Too low.")
        if player_guess == game_number:
            has_won = True
            return print("You win!")
    # Takes guesses from the player while they still have lives, they lose a life for every wrong guess    
    while has_won == False:
        if difficulty == 'easy':
            player_lives = 10
            while player_lives > 0 and has_won == False:
                game()
                player_lives -= 1
                # for easy and hard, only prints remaining lives if they guessed wrong.
                if has_won == False:
                    print(f"You have {player_lives} attempts remaining.")

        elif difficulty == 'hard':
            player_lives = 5
            while player_lives > 0 and has_won == False:
                game()
                player_lives -= 1
                if has_won == False: 
                    print(f"You have {player_lives} attempts remaining.")
        # game over
        if player_lives == 0 and has_won == False:
            print("Out of lives. You lose.")
            break
    # asks if the player wants to play again
    play_again_question = str(input("Would you like to play again? Type 'yes' or 'no': "))
    if play_again_question == 'yes':
        play_again = True
    elif play_again_question == 'no':
        play_again = False

