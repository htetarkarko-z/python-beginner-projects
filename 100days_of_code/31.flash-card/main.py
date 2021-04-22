from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data_table = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_csv(orient='records')
else:
    to_learn = data_table.to_dict(orient='records')


# -----------------------------CHANGE CARDS---------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bgimg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# ------------------------------FLIP CARDS----------------------------------- #
def flip_card():
    canvas.itemconfig(card_bgimg, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


# ------------------------------KNOWN CARDS---------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

# -----------------------------------UI-------------------------------------- #
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_bgimg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(
    image=wrong_img, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(
    image=right_img, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
