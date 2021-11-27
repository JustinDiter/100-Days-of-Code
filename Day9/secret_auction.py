from auction_art import logo
import os
# function to clear the console on windows
clear = lambda: os.system('cls')

print(logo)

print("Welcome to the silent auction.")
# where the dictionaries containing the name and bid price of each bidder will be stored
bidders = []
# loop flag while there are still bidders to input
other_bidders = True
while other_bidders:
    # function that takes the name and price of each bidder and creates a dictionary entry for them
    def add_bidder(name, bid):
        add_bidder = {
            "Name" : name,
            "Bid" : bid,
        }
        # adds the dictionary entry to the bidders list
        bidders.append(add_bidder)

    bidder_name = input("Type the name of the bidder :\n")
    bidder_price = input(f"Type the ammount that {bidder_name} would like to bid in dollars :\n")
    # uses the function to create dictionary entry with given name and price
    add_bidder(name=bidder_name,bid=bidder_price)
    # loops the function as long as there are still bidders
    another_bidder_response = input("Is there another bidder ? Y/N : \n").lower()
    if another_bidder_response == "n":
        other_bidders = False
    # clear function called (only works for windows sorry)
    clear()
    
# finds the highest bidder among the dictionaries in the bidders list, stores the whole information in the dictionary in the variable to be able to call name and price individually
highest_bidder = max(bidders, key= lambda x:x['Bid'])

print(f"The highest bidder is {highest_bidder['Name']} with a bid of ${highest_bidder['Bid']}.")





