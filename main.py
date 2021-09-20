from tkinter import *
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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED, bg=PINK, )
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=YELLOW, bg=PINK, )
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=PINK, )

    # countdown(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# EVENT DRIVEN
# CREATING COUNTDOWN TIMER
def countdown(count):
    global reps
    count_min = math.floor(count / 60)  # this will enable rounding down, largest whole number less than
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")  # lets me change elements within a canvas item
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # creating screen
window.title("Maru Timer")
window.config(padx=100, pady=50, bg=PINK)

# Label at the top, big text
timer_label = Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 50), highlightthickness=0)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)  # making a canvas with the even dimensions of
# the image
tomato_img = PhotoImage(file='tomato.png')  # getting a hold of the tomato image
canvas.create_image(100, 112, image=tomato_img)  # adding the image to the canvas & setting it in the middle of screen

# time text
time_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# left Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Right Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# label keeps track of how many we've run
check_marks = Label(fg=GREEN, bg=PINK)  # copied & pasted check mark image from wiki
check_marks.grid(column=1, row=3)

window.mainloop()  # ensuring screen stays on
