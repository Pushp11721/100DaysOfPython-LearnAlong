from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
#----------------------------------------------GENERATE WORDS------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card={}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    random_word = current_card["French"]
    canvas.itemconfig(word, text=random_word,fill="black")
    canvas.itemconfig(language, text="French",fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000,flip_card)


def flip_card():
    canvas.itemconfig(language,text="English",fill="white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=0)
    print(len(to_learn))
    next_card()

#----------------------------------------------UI------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

#card
canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
language = canvas.create_text(400,150,text="",fill="black",font=("Arial",40,"italic"))
word = canvas.create_text(400,263,text="", fill="black", font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

#wrong
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

#right
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()