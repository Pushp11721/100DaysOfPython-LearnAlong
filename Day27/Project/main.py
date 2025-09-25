#TODO : Mile to Kilometers Converter Project
from tkinter import *

from streamlit import columns

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)

#Entries - Miles & Km
miles = Entry(width=20)
miles.grid(column=1,row=0)

#Labels - Miles & Km
miles_l = Label(text="Miles")
km_l = Label(text="Km")
km = Label(text=0)
km.grid(column=1,row=1)
is_equal_to = Label(text="is equal to")
miles_l.grid(column=2,row=0)
km_l.grid(column=2,row=1)
is_equal_to.grid(column=0,row=1)

#Button - convert
def miles_to_km():
    m_value = miles.get()
    ans = float(m_value) * 1.60934
    ans_1 = round(ans,2)
    km.config(text=f"{ans_1}")

convert = Button(text="Calculate",command=miles_to_km)
convert.grid(column=1,row=2)

window.mainloop()