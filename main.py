from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARD GENERATOR ------------------------------- #
data_file = pd.read_csv('../data/french_words.csv')
french_dict = data_file.to_dict()


def change_word():
    global study_word
    new_num = random.randint(0, 100)
    canvas.delete(study_word)
    study_word = canvas.create_text(400, 263, text=french_dict['French'][new_num], font=('Ariel', 60, 'bold'))


# ----------------------------- SAVE RESULTS -------------------------------- #
# ----------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file='../images/card_front.png')
card_back = PhotoImage(file='../images/card_back.png')

canvas = Canvas(width=800, height=550)
canvas.create_image(2, 1, image=card_front, anchor='nw')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400, 150, text='French', font=("Ariel", 40, 'italic'))

study_word = canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))

x_image = PhotoImage(file='../images/wrong.png')
incorrect_button = Button(text='Incorrect', image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                          command=change_word)
incorrect_button.grid(column=0, row=1)

check_image = PhotoImage(file='../images/right.png')
correct_button = Button(text='Correct', image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                        command=change_word)
correct_button.grid(column=1, row=1)

window.mainloop()
