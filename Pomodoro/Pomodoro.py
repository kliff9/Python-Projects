from tkinter import *
from tkinter import font
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

myTimer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(myTimer)
    canvas.itemconfig(timer_text, text="0:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

    


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps   
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    Long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        Timer(Long_break)
        label.config(text="Long break", fg=RED)

    elif reps % 2 == 0:
        Timer(short_break)
        label.config(text="Short break", fg=PINK)

    else:
        Timer(work_sec)
        label.config(text="Working", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#cant use while loops?
def Timer(count):
    count_min = math.floor(count / 60 )
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    # elif count_min == 0:
    #     count_min = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}" 
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0: 
        global myTimer
        myTimer = window.after(1000, Timer, count- 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+= "✔️"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


## Photo
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #highlight thinks get rid of the "border"
tomato_img = PhotoImage(file=r"Pomodoro\tomato.png")

canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=2, row=2)

timer_text= canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))

def action():
    print('clicked')
button = Button(text="Reset", command=reset)
button.grid(column=4, row=4)

button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=4)

label = Label(text="Timer", font=(FONT_NAME, 44), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(column=2, row=0) 

check_marks = Label(text="", highlightthickness=0, bg=YELLOW )
check_marks.grid(column=2, row=5) 






window.mainloop()