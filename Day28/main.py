import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
    global TIMER
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")#Reset timer text
    timer.config(text="Timer", fg=GREEN)#Reset label
    checkmark.config(text="")#Reset checkmark
    global REPS
    REPS = 0 #Reset reps

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break",fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)#floor() - return greatest integer less than that number
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#Canvas method - to apply background image
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")#It can read through file to hold image
canvas.create_image(100,112,image=tomato_img)#takes pixel width and height

timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME,30,"bold"))

canvas.grid(column=1,row=1)

#Label
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME,40,"bold"), bg=YELLOW)
timer.grid(column=1,row=0)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,10,"bold"))
checkmark.grid(column=1,row=3)

#Buttons
start = Button(text="Start",command=start_timer)
start.grid(column=0,row=2)
reset = Button(text="Reset",command=reset_time)
reset.grid(column=2,row=2)

#"✔"

window.mainloop()