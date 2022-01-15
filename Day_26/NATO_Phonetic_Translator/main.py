import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

# Creates a dictionary of the letters of the alphabet as the keys and the phonetic alphabet equivalent using comprehension
for (index, row) in df.iterrows():
    Phonetic_Alphabet = {str(row.letter):str(row.code) for (index, row) in df.iterrows()}

# For testing purposes
# print(Phonetic_Alphabet) 

# The user inputs a word and a list of the word translated to the NATO Phonetic Alphabet is created using comprehension and 
user_word = input("Input a word to translate in the NATO phonetic alphabet: ")
user_word_translated = [Phonetic_Alphabet[c.upper()] for c in user_word]

print(user_word_translated)

