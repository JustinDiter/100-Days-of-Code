from tkinter import *

# Window GUI Config
window = Tk()
window.minsize(width=300,height=100)
window.title("GUI !")
window.config(padx=20,pady=20)

def calculate_distance():
    '''Does the conversion from miles to km rounded to 2 decimal points, then changes the text of km_distance to display
    that value'''
    miles_distance = float(miles_input.get()) * 1.61
    miles_distance = "{:.2f}".format(miles_distance)
    km_distance["text"] = miles_distance

# Different elements displayed in the window and their coordinates in the grid

miles_label = Label(text='is equal to:', font=('Courier', 12, "normal"))
miles_label.grid(row=1,column=0)

calculate_button = Button(text="Calculate", command=calculate_distance)
calculate_button.grid(row=2,column=1)

miles_label = Label(text='Miles', font=('Courier', 12, "normal"))
miles_label.grid(row=0,column=2)

km_distance = Label(text='0',font=('Courier', 12, "normal"))
km_distance.grid(row=1,column=1)

km_label = Label(text='Km', font=('Courier', 12, "normal"))
km_label.grid(row=1,column=2)

miles_input = Entry()
miles_input.grid(row=0,column=1)

# Keeps the window open
window.mainloop()
