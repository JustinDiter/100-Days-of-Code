from auction_art import logo
import os

clear = lambda: os.system('cls')

print(logo)

print("Welcome to the silent auction.")

bidders = []
other_bidders = True
while other_bidders:
    def add_bidder(name, bid):
        add_bidder = {
            "Name" : name,
            "Bid" : bid,
        }
        bidders.append(add_bidder)

    bidder_name = input("Type the name of the bidder :\n")
    bidder_price = input(f"Type the ammount that {bidder_name} would like to bid in dollars :\n")

    add_bidder(name=bidder_name,bid=bidder_price)

    another_bidder_response = input("Is there another bidder ? Y/N : \n").lower()
    if another_bidder_response == "n":
        other_bidders = False
    clear()
    

highest_bidder = max(bidders, key= lambda x:x['Bid'])

print(f"The highest bidder is {highest_bidder['Name']} with a bid of ${highest_bidder['Bid']}.")





