import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage
import pygame

       
pygame.mixer.init()# initialise the pygame

root["bg"] = "#333"

s = ttk.Style()
s.configure("TButton", font=("Ubintu", 16))

grid_layiut = ttk.Frame(root)
grid_layiut.pack(pady=10)

cycles, count = 1, 1
skipped = False
stopped = False
running = False

schedule = [
    ("Work", 5, "pink"),
    ("Break", 3, "yellow"),
    ("Rest", 8, "light green"),
    ("Work", 1500, "pink"),
    ("Break", 300, "yellow"),
    ("Work", 1500, "pink"),
    ("Break", 300, "yellow"),
    ("Work", 1500, "pink"),
    ("Break", 300, "yellow"),
    ("Rest", 1800, "light green")
]


pomodoro_condition_label = ttk.Label(grid_layiut, text="Work", font=("Ubuntu", 16), background="pink")
pomodoro_condition_label.grid(row=1, column=1, sticky="sw")

pomodoro_timer_label = ttk.Label(grid_layiut, text="25:00", font=("Ubuntu", 64), background="pink")
pomodoro_timer_label.grid(row=2, column=1, rowspan=4, sticky="n")

start_button = ttk.Button(grid_layiut, text="Start", command=start_thread)
start_button.grid(row=1, column=0)

pause_button = ttk.Button(grid_layiut, text="Pause", command=pause)
pause_button.grid(row=2, column=0)

skip_button = ttk.Button(grid_layiut, text="Skip", command=skip)
skip_button.grid(row=3, column=0)

repeat_button = ttk.Button(grid_layiut, text="Repeat", command=repeat)
repeat_button.grid(row=4, column=0)

reset_button = ttk.Button(grid_layiut, text="Reset", command=reset)
reset_button.grid(row=5, column=0)

pomodoro_counter_label = ttk.Label(grid_layiut, text="Pomodoro: 0:0", font=("Ubuntu", 16))
pomodoro_counter_label.grid(row=6, column=0, columnspan=2)

root.mainloop()


def start_thread():
    t = threading.Thread(target=timer(*schedule[0]))
    t.start()
    running = True

def timer(condition, full_seconds, colour):  
    while full_seconds >= 0 and not stopped:
        minutes, seconds = divmod(full_seconds, 60)
        pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.update()
        time.sleep(1)
        full_seconds -= 1
    else:
        pomodoros_stwich(condition, full_seconds, colour)
        start(condition, full_seconds, colour)
    return condition, full_seconds, colour
        
def pomodoros_stwich(condition, full_seconds, colour):   
    print("Pomodoro_srwitch()")
    if condition == "Work":
        count += 1
    else:
        count = 0
        cycles += 1 
    # stwich pomodoro
    condition, full_second, colour = schedule.pop(0)
    schedule.append(condition, full_seconds, colour)
    
    minutes, seconds = divmod(full_seconds, 60)
    pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}", background=colour)

    pomodoro_condition_label.config(text=condition, background=colour)
    pomodoro_counter_label.config(text=f"Pomodoeos: {cycles}:{count}")
    root.update()


def start(condition, full_second, colour):
    print("Begin Start()")
    stopped = False
    skipped = False            
    print("End Start()")


def pause():
    pass

def skip():
    pass

def repeat():
    pass

def reset():
    pass

