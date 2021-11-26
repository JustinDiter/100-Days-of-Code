alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from caesar_cipher_art import logo

print(logo)
# Flag that changes to False when the user is finished with the program
should_continue = True
# The loop that allows the user to use the program as many times in a row as they want
while should_continue:
    # User inputs for the cipher parameters
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    #the cipher function
    def caesar(text, shift):
        # turns the text into a list so that the program can manipulate and change elements of the string
        text_as_list = list(text)
        # turns the shift into a negative if the user wants to decode
        if direction == 'decode':
            shift *= -1
        # for every character in the text (...)
        for letter in range(len(text_as_list)):
            # skips over anything that isn't a letter
            if text_as_list[letter] not in alphabet:
                continue
            # takes every letter of the text, finds the index of it in alphabet and adds the shift, % 26 is to have the list loop back to the first element if the index goes over the length of alphabet[]
            letter_to_manipulate = text_as_list[letter]
            index_of_manipulated_letter = alphabet.index(letter_to_manipulate) + shift
            text_as_list[letter] = alphabet[index_of_manipulated_letter % 26]
        # joins all of the elements of the list back into a string    
        text_as_list = ''.join(text_as_list)
        # naming initial text that was changed to a descriptive name for comprehension
        manipulated_text = text_as_list        
        # the final output
        print(f"The {direction}d text is {manipulated_text}.")


    caesar(text, shift)
        
    response = input("Would you like to start again ? Y/N :\n").lower()
    if response == "n":
        should_continue = False
        
               
        

    
