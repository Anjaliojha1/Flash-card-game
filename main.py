from tkinter import *
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
#-------------------Read CSV file ------------------#
try:
    data = pd.read_csv("french_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def new_flashcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back)

def is_known():
    to_learn.remove(current_card)
    data1 = pd.DataFrame(to_learn)
    data1.to_csv("words_to_learn.csv", index=False)
    new_flashcard()


#------------------GUI-----------------#


window = Tk()
window.title("Flashy")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front = PhotoImage(file="card_front.png")
back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.create_image(400, 263, image=back)
canvas.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="right.png")
button1 = Button(image=right, highlightthickness=0, command=is_known)
button1.grid(column=1, row=1)

wrong = PhotoImage(file="wrong.png")
button2 = Button(image=wrong, highlightthickness=0, command=new_flashcard)
button2.grid(column=0, row=1)

new_flashcard()

window.mainloop()
