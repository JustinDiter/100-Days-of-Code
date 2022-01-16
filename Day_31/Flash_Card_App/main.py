import pandas as pd
import random
from tkinter import *

# ---------------------------- DATAFRAME ---------------------
# Checks if there's a file containing the words that haven't been learned yet
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/spanishenglish.csv")
# makes a dictionary from the df with {'spanish word' : 'english word'} as (key, value)
vocab_dict = pd.Series(df.english.values, index=df.spanish).to_dict()
# current random vocab word saved in variable
random_vocab_word = None
# ---------------------------- GENERATE RANDOM VOCAB ----------
def random_vocab():
    global random_vocab_word
    random_vocab_word = random.choice(list(vocab_dict.keys()))
    # changes the text on the flashcard to the randomly chosen vocab word
    canvas.itemconfig(vocab_text, text=f"{random_vocab_word}")
# ---------------------------- NEXT CARD ---------------------
def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    random_vocab()
    # changes the flashcard appearance back to the front and gives new word
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language_text, text="Spanish", fill="black")
    canvas.itemconfig(vocab_text, text=f"{random_vocab_word}", fill="black")
    # resets the timer to flip the card
    flip_timer = window.after(3000, flip_card)
# ---------------------------- FLIP CARD ---------------------
def flip_card():
    global random_vocab_word
    # changes the flashcard appearance as if flipped with translation of the word on the front 
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(vocab_text, text=f"{vocab_dict[random_vocab_word]}", fill="white")
# ---------------------------- ADD WORD TO LIST TO LEARN -----
def add_word():
    # creates or updates the correctly formatted words_to_learn.csv file in the data folder
    # with the list of words that were not removed for being known
    new_df = pd.DataFrame(vocab_dict.items(), columns=['spanish', 'english'])
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- REMOVE KNOWN WORD -------------
def remove_word():
    # removes the current word from the df if known
    # = pressed on green check
    vocab_dict.pop(random_vocab_word)
    next_card()
# ---------------------------- UI ----------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Spanish to English Flashcards")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

# CARD FRONT
card_front_image = PhotoImage(file="./images/card_front.png")

# CARD BACK
card_back_image = PhotoImage(file="./images/card_back.png")

# CANVAS
canvas = Canvas(height=526, width=800, bg= BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(0,0, image=card_front_image, anchor="nw")
language_text = canvas.create_text(400, 150, text="Spanish", fill="black", font=("Ariel", 40, "italic"))
vocab_text = canvas.create_text(400, 263, text="Place holder", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

# BUTTONS
cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=add_word)
cross_button.grid(row=1,column=0)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=remove_word)
check_button.grid(row=1,column=1)
# ---------------------------- PILOT CODE --------------------
random_vocab()
# flips the card over after 3 seconds
flip_timer = window.after(3000, flip_card)

window.mainloop()
