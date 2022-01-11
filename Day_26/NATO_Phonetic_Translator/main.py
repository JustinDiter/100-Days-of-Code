import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

for (index, row) in df.iterrows():
    Phonetic_Alphabet = {str(row.letter):str(row.code) for (index, row) in df.iterrows()}

print(Phonetic_Alphabet)

user_word = input("Input a word to translate in the NATO phonetic alphabet: ")
user_word_translated = [Phonetic_Alphabet[c.upper()] for c in user_word]

print(user_word_translated)

# translated_list = [value for (key, value) in Phonetic_Alphabet.items() for letter in user_word_formatted if key == letter]
# print(translated_list)
