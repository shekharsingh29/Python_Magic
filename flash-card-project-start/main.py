from email.mime import image
from tkinter import *
from turtle import title
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
print(data)
print("\n\n")
trans_data = data.to_dict(orient="records")
print(trans_data)
random_card = {}

def show_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(trans_data)
    canvas.itemconfig(title_text, text="FRENCH")
    canvas.itemconfig(word_text, text=random_card["French"])
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=random_card["English"])
    canvas.itemconfig(image = card_back_image)

def known_answer():
    trans_data.remove(random_card)
    data = pandas.DataFrame(trans_data)
    print(data)
    data.to_csv("data/words_to_learn",index=False)
    show_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=536)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 60, "bold"))
word_text = canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=show_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_answer)
known_button.grid(row=1, column=1)

show_card()

window.mainloop()