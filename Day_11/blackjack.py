import os
import random
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Initializes the game
play = input("Would you like to play a game of Blackjack ? Type 'yes' or 'no': ")
if play == 'yes':
    # Custom windows clear function
    clear = lambda: os.system('cls')
    # Loop flag
    play_again = True

    while play_again:
        # Prints blackjack ascii art
        print(logo)
        # deals two random cards to the player and the dealer
        player_cards = [random.choice(cards), random.choice(cards)]
        dealer_cards = [random.choice(cards), random.choice(cards)]

        # gives a numerical score depending on the cards in each hand
        player_score = sum(player_cards)
        dealer_score = sum(dealer_cards)

        # flag that ends the game when turned to True
        scores_compared = False
        # function that compares the hands of the player and the dealer, also adding cards to the dealer's hand if needed
        def compare_scores():
            dealer_score = sum(dealer_cards)
            if dealer_score == 21:
                "    Blackjack! You lose."
            if dealer_score >= 17:            
                print(f"    The dealer's cards are {dealer_cards}, for a score of: {dealer_score}")
            while dealer_score < 17:
                # adds cards to dealer's hand until their score is over 17
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)
                print(f"    The dealer's cards are {dealer_cards}, for a score of: {dealer_score}")
            # switches the value of the ace to 1 if the hand will bust otherwise
            if cards[0] in dealer_cards:
                if dealer_score > 21:
                    dealer_score -= 10
                    print(f"The dealer's ace is now worth 1 point to avoid a bust, for a score of {dealer_score}.")
            if dealer_score > 21:
                return print("    You win!")
            if player_score > dealer_score:
                return print("    You win!")
            elif player_score == dealer_score:
                return print("    Draw.")
            else:
                return print("    You lose.")
        # gives the base console prints for the game    
        print(f"    Your cards are {player_cards}, for a score of: {player_score}")
        print(f"    The dealer's first card is {dealer_cards[0]}.")
        # two aces in player's hand case
        if player_score == 22:
            player_score -= 10
            print(f"    One of your aces is now worth 1 point to avoid a bust, for a score of {player_score}.")
        # player blackjack, but checks if the dealer doesn't also have blackjack before declaring if the player won
        if player_score == 21:
            if dealer_score == 21:
                print(f"    Blackjack! But the dealer also has Blackjack with {dealer_cards}, so you lose.")
            else:
                print("    Blackjack ! You win.")
        # Let's player pick a total of 4 cards as long as they are under 21
        while player_score < 21 and not scores_compared:
            
            another_card_answer = input("Would you like another card ? Type 'yes' or 'no': ")

            if another_card_answer == 'yes':
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                print(f"    Your cards are {player_cards}, for a score of: {player_score}")
                if player_score < 21:
                    another_card_answer = input("Would you like another card ? Type 'yes' or 'no': ")
                    if another_card_answer == 'yes':
                        player_cards.append(random.choice(cards))
                        player_score = sum(player_cards)
                        print(f"    Your cards are {player_cards}, for a score of: {player_score}")
            # switches ace value if hand will bust otherwise
            if cards[0] in player_cards:
                if player_score > 21:
                    player_score -= 10
                    print(f"    Your ace is now worth 1 point to avoid a bust, for a score of {player_score}.")
            # player's hand is a bust.
            if player_score > 21:
                print("    Bust! You lose.")
            # compares the two hands once the player is done adding cards and they haven't lost, while ending the game once the hands are compared and a winner is declared
            else:
                compare_scores()
                scores_compared = True
        # Game loop if the player wants to play again
        play_again_question = input("Would you like to play again ? Type 'yes' or 'no': ")
        if play_again_question == 'yes':
            clear()
        if play_again_question == 'no':
            play_again = False
