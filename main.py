from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARD GENERATOR ------------------------------- #
# ----------------------------- SAVE RESULTS -------------------------------- #
# ----------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=550)
card_front = PhotoImage(file='../images/card_front.png')
card_back = PhotoImage(file='../images/card_back.png')
canvas.create_image(2, 1, image=card_front, anchor='nw')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

x_image = PhotoImage(file='../images/wrong.png')
incorrect_button = Button(text='Incorrect', image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0)
incorrect_button.grid(column=0, row=1)

check_image = PhotoImage(file='../images/right.png')
correct_button = Button(text='Correct', image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0)
correct_button.grid(column=1, row=1)

window.mainloop()
