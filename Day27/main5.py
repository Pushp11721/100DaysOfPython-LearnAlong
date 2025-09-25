from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#Label
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack()
#we can also change label properties
my_label["text"]="new text"
my_label.config(text="New text")

def button_clicked():
    new_text = input_i.get()
    my_label.config(text=new_text)

#Button
button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry
input_i = Entry(width=10)
input_i.pack()
#new_label = input_i.get()#this will return input

window.mainloop()