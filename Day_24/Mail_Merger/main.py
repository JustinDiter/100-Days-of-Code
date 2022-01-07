# takes the file with the character names and returns them as a list, join and split remove the \n in every index, could have also used .strip()
with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    names = ''.join(names)
    names = names.split()

# stores the template letter as a variable
with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

# for every name in the list of name, replace the [name] placeholder with the correct name and create the letter as a separate text file in the Output folder
for name in names:
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/{name}_letter.txt", mode="a") as file:
        personalized = starting_letter.replace("[name]",name)
        file.write(f"{personalized}")
