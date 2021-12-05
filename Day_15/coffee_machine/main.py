from menu_resources import MENU, resources 

# power off flag
power_off = False

#power off loop
while not power_off:
    user_choice = input("What would you like? (espresso, $1.5/latte, $2.5/cappuccino, $3.0): ")
    # technician power off switch
    if user_choice == 'off':
        power_off = True
    # gives a report of the ingredient levels in the machine
    # gives a report of the money in the machine if there is any
    if user_choice == 'report': 
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}mg")
        if "money" in resources:
            print(f"Money: ${resources['money']}")

    # pay function, calculates change and returns if the machine was
    # given more change than the cost of the drink.
    # if not given enough, refunds.
    # creates money key in resources dictionary if first
    # successful purchase
    def pay():
        '''adds up the coins inserted into the machine by the user
        and gives them back their change if needed'''
        quarters = 0.25 * int(input("How many quarters will you insert?: "))
        dimes = 0.1 * int(input("How many dimes will you insert?: "))
        nickels = 0.05 * int(input("How many nickels will you insert?: "))
        pennies = 0.01 * int(input("How many pennies will you insert?: "))
        sum_coins = quarters + dimes + nickels + pennies
        if sum_coins < MENU[user_choice]['cost']:
            return print("Not enough for purchase. Money refunded.")
        if sum_coins >= MENU[user_choice]["cost"]:
            user_change = sum_coins - MENU[user_choice]["cost"]
            if "money" not in resources:
                resources["money"] = 0
            resources["money"] += MENU[user_choice]["cost"]
            print(f"Here is your change: ${round(user_change, 2)}")
            return print(f"Here is your {user_choice}, enjoy!")
            
    # if user correctly chooses a drink from the menu and
    # there are enough ingredients in the machine to make the drink,
    # take their money and start the transaction
    if user_choice in MENU:
        resources_insufficient = False
        for ingredient, ingredient_value in MENU[user_choice]['ingredients'].items():
            if ingredient in resources:
                if ingredient_value <= resources[ingredient]:
                    resources[ingredient] -= ingredient_value 
                else:
                    print(f"{ingredient.title()} low.")
                    resources_insufficient = True
        if not resources_insufficient:
            pay()
