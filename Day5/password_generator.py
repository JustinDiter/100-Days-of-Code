import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize the blank password, and give a random selection of letters, symbols, and numbers depending on user input

password = ""

# Give the amount of random letters specified
for letter in range (0, nr_letters) :
    password += str(random.choice(letters))

# Give the amount of random symbols specified
for symbol in range (0, nr_symbols) :
    password += str(random.choice(symbols))

# Give the amount of random numbers specified
for number in range (0, nr_numbers) :
    password += str(random.choice(numbers))

# Scrambling all of the characters randomly to exponentially increase complexity of the generated password
random_password = ''.join(random.sample(password, len(password)))
print(random_password)
