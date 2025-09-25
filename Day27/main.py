#TODO : Tkinter - Graphical User Interface (GUI)
import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")#Giving title to window
window.minsize(width=500 ,height=300)# We can set default size for window unless we/user want to change it

#TODO : Label
my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))#It is not enough to display on window,
# we have to specify how component is going to show up on display
my_label.pack(expand=True)#centre-default

window.mainloop()#To keep the window on screen. This line of code should always be in the end of the program
