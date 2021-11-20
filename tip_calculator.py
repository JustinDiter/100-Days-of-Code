print("Welcome to the tip calculator !")

# The price of the meal
bill = float(input("What was the total bill ? $"))

# The tip you would like to leave
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ? "))

# The amount of people splitting the bill
people = int(input("How many people are splitting the bill ? "))

# What everyone will pay, taking the bill and multiplying it by 1.[percentage] and
# dividing it by the amount of people who will be paying the bill, giving the final
# amount rounded to the nearest full cent.

amount_per_person = round(float(bill * (1 + (tip / 100)) / people),2)
amount_per_person = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${amount_per_person}")