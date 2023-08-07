from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#FF3612"
GREEN = '#9bdeac'
BLUE = "#0C06FF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 0.4
APP_BG = "black"
BUTTON_FONT = ("harlow solid italic", 15, "italic")
timer_count = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_button_func():
    screen.after_cancel(timer_count)
    # reset timing text to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # reset top label text back to initial (timer)
    timer.config(text="Timer")
    # reset checkmarks.
    check.config(text=" ")
    global switch_times
    switch_times = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
switch_times = 0


def start_button_timer():
    global switch_times
    switch_times += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if switch_times % 8 == 0:
        count_down_mechanism(long_break_sec)
        timer.config(text="Long Break", font=("bauhaus 93", 50, "bold"), fg="black")
    elif switch_times % 2 == 0:
        count_down_mechanism(short_break_sec)
        timer.config(text="Break", font=("broadway", 50, "bold"), fg="magenta")
    elif switch_times % 1 == 0:
        count_down_mechanism(work_sec)
        timer.config(text="Working", font=("britannic bold", 50, "bold"), fg=BLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
mark = ""


def count_down_mechanism(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count > 0:
        global timer_count
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
        timer_count = screen.after(1000, count_down_mechanism, count-1)
    else:
        start_button_timer()
        if switch_times % 2 == 0:
            global mark
            mark += "✓"
            check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


screen = Tk()
screen.title("My_Pomodoro_App")
screen.config(padx=100, pady=50, bg=GREEN)

# Creating canvas with image and text
canvas = Canvas(width=210, height=225, bg=GREEN, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=image)
timer_text = canvas.create_text(105, 130, text="00:00", fill="black", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Creating timer Label
timer = Label(bg=GREEN)
timer.config(text="Timer", font=("algerian", 50, "bold"))
timer.grid(row=0, column=1)


# Creating start button
start_button = Button(bg=PINK)
start_button.config(text="Start", font=BUTTON_FONT, command=start_button_timer)
start_button.grid(column=0, row=2)

# Creating reset button
reset_button = Button(bg=PINK)
reset_button.config(text="Reset", font=BUTTON_FONT, command=reset_button_func)
reset_button.grid(column=2, row=2)

# creating check label
check = Label(bg=GREEN, fg="black", highlightthickness=0)
check.config(text=" ", font=("bauhaus 93", 20, "bold"))
check.grid(row=3, column=1)

screen.mainloop()
