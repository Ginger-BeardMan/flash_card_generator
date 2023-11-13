from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARD GENERATOR ------------------------------- #
try:
    data_file = pd.read_csv('data/words_to_learn.csv')
    french_dict = data_file.to_dict(orient='records')
except FileNotFoundError:
    data_file = pd.read_csv('data/french_words.csv')
    french_dict = data_file.to_dict(orient='records')

current_card = {}
unknown_card_list = []
known_card_list = []


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict)
    if current_card in known_card_list:
        change_word()
    else:
        canvas.itemconfig(card_background, image=card_front)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(study_word, text=current_card['French'], fill='black')
        flip_timer = window.after(3000, func=flip_card)
        print(known_card_list)


def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(study_word, text=current_card['English'], fill='white')


# ----------------------------- SAVE RESULTS -------------------------------- #

def save_known():
    known_card_list.append(current_card)


def save_unknown():
    if current_card not in unknown_card_list:
        unknown_card_list.append(current_card)
        study_data = pd.DataFrame(unknown_card_list)
        study_data.to_csv('data/words_to_learn.csv', mode='w', index=False)

# ----------------------------- UI SETUP ------------------------------------ #


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file='../images/card_front.png')
card_back = PhotoImage(file='../images/card_back.png')

canvas = Canvas(width=800, height=550)
card_background = canvas.create_image(2, 1, image=card_front, anchor='nw')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, 'italic'))

study_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

x_image = PhotoImage(file='../images/wrong.png')
unknown_button = Button(text='Incorrect', image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                        command=lambda: [save_unknown(), change_word()])
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file='../images/right.png')
known_button = Button(text='Correct', image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                      command=lambda: [save_known(), change_word()])
known_button.grid(column=1, row=1)

change_word()

window.mainloop()

