from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .5
SHORT_BREAK_MIN = .2
LONG_BREAK_MIN = .6
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# stop timer on screen, change it to start value, change title label, reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_mark.config(text='')


# ------------------------- TIMER MECHANISM ---------------------------- #
# start the countdown increase reps with 1 and check what rep your in and make
# accronding
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ------------------------- COUNTDOWN MECHANISM ---------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_sec < 10:  # for extra zero in front
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:  # if count parameter is passed the start the func
        timer = window.after(1000, count_down, count - 1)
    else:  # if count is completed start automatic and add check mark
        start_timer()
        mark = ''
        wrok_sessions = math.floor(reps / 2)
        for i in range(wrok_sessions):
            mark += '✓'
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.resizable(0, 0)
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)

timer_text = canvas.create_text(100, 138, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()
