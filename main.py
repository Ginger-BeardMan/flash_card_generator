from tkinter import *
import random
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARD GENERATOR ------------------------------- #
data_file = pd.read_csv('../data/french_words.csv')
french_dict = data_file.to_dict(orient='records')


def change_word():
    new_word = random.choice(french_dict)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(study_word, text=new_word['French'])
    window.update()
    time.sleep(3)
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(study_word, text=new_word['English'])


# ----------------------------- SAVE RESULTS -------------------------------- #
# ----------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file='../images/card_front.png')
card_back = PhotoImage(file='../images/card_back.png')

canvas = Canvas(width=800, height=550)
card_background = canvas.create_image(2, 1, image=card_front, anchor='nw')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, 'italic'))

study_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

x_image = PhotoImage(file='../images/wrong.png')
incorrect_button = Button(text='Incorrect', image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                          command=change_word)
incorrect_button.grid(column=0, row=1)

check_image = PhotoImage(file='../images/right.png')
correct_button = Button(text='Correct', image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                        command=change_word)
correct_button.grid(column=1, row=1)

change_word()

window.mainloop()
