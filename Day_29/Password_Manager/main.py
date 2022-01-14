import random
import pyperclip
from tkinter import *
from tkinter import messagebox
FONT = ("Courier", 12, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(12,16) 
    nr_symbols = random.randint(4,8)
    nr_numbers = random.randint(4,8)

    # Initialize the blank password, and give a random selection of letters, symbols, and numbers depending on user input

    password = ""

    password += ''.join([str(random.choice(letters)) for letter in range(0, nr_letters)])

    password += ''.join([str(random.choice(symbols)) for symbol in range(0, nr_symbols)])

    password += ''.join([str(random.choice(numbers)) for symbol in range(0, nr_numbers)])

    randomized_password = ''.join(random.sample(password, len(password)))
    password_entry.insert(END, string=f"{randomized_password}")
    pyperclip.copy(randomized_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    
    # Error messages if blank fields
    if website == "":
        messagebox.showerror(title="Error", message="No website entered.")
        return
    
    if email_username == "":
        messagebox.showerror(title="Error", message="No email or username entered.")
        return
    
    if password == "":
        messagebox.showerror(title="Error", message="No password entered.")
        return
    
    # Asks if information is correct, if not, let's user change it
    confirmed = messagebox.askyesno(title='Confirmation', message=f"Save information as entered?\nWebsite: {website}\nEmail or Username: {email_username}\nPassword: {password}")
    
    if confirmed:    
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file='logo.png')

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=1, sticky="w")

# Website + Entry
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username + Entry
email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=45)
email_username_entry.insert(0, "example@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

# Password + Entry 
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=1)

# Button to generate random strong password
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=2, columnspan=2)

# Button to add entered information to passwords.txt located in local folder
add_password_button = Button(text="Add", width=38, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
