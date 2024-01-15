from tkinter import *
from tkinter import messagebox
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

    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(time_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    if reps == 7:
        title_label.config(text="Break", fg=RED)
        messagebox.showinfo(title="BREAK", message="Hey, is time for  break")
        reps += 1
        countdown(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        title_label.config(text="Work", fg=GREEN)
        messagebox.showinfo(title="Work Time", message=f"Let's work")
        reps += 1
        countdown(WORK_MIN * 60)

    else:
        title_label.config(text="Break", fg=PINK)
        messagebox.showinfo(title="BREAK", message=f"Hey, is time for  break")
        reps += 1
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = f"00{math.floor(count / 60)}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    if count == 0:
        start()
    if reps % 2 == 0:
        mark = []
        mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=YELLOW, font=FONT_NAME, highlightthickness=0, command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, font=FONT_NAME, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=15)
check_marks.grid(row=3, column=1)

window.mainloop()
