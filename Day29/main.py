from tkinter import *
from tkinter import messagebox #this is not a class that's why we have to import it separately
from random import randint, choice, shuffle
import pyperclip #This module is for copying something to the clipboard directly without doing anything
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)
    password_entry.insert(0,string=random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #Create a dictionary to pass on to json file format
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if website=="":
        messagebox.showerror(title="Oops!",message="You can't left Website empty")
    elif email=="":
        messagebox.showerror(title="Oops!", message="You can't left Email empty")
    elif password=="":
        messagebox.showerror(title="Oops!", message="You can't left Password empty")
    else:
        #TODO : update data format to JSON
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)#read
        except FileNotFoundError:
            with open("data.json",mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)#write
        else:
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                json.dump(data, data_file, indent=4)#write
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(0, string="abc@gmail.com")

# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Canvas method to apply background image
canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Entries
website_entry = Entry(width=34)
website_entry.grid(column=1,row=1)
website_entry.focus()#This will start with cursor on website entry
email_entry = Entry(width=53)
email_entry.insert(0,string="abc@gmail.com")#Adding common entry value for email
email_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(column=1,row=3)

#Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)
add_button = Button(text="Add",width=45,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search",width=15,bg="blue",command=find_password)
search_button.grid(column=2,row=1)


window.mainloop()