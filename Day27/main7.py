#TODO : pack(), place(), grid()
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)#Adding padding

#Label
my_label = Label(text="I am a label",font=("Arial",24,"bold"))
my_label.config(text="New Text")
# my_label.place(x=250,y=0)#place - coordinates
#If we have too many widgets, it will become really difficult to place them by place() i.e. coordinates
#So we can use grid()
my_label.grid(column=0,row=0)#it is relative to other widgets
my_label.config(padx=50,pady=50)

def button_clicked():
    my_label.config(text="hello")
#Button
button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)
button_1=Button(text="New Button")
button_1.grid(column=3,row=0)

#Entry
input_i = Entry(width=10)
print(input_i.get())
input_i.grid(column=4,row=2)




window.mainloop()

#We can't mix these methods - we can only use one from them for the entir code