import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

    
root = tk.Tk()

root.geometry("340x180")
root.title("Pomodoro Timer")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="tomato.png"))
root["bg"] = "#333"

s = ttk.Style()
s.configure("TButton", font=("Ubintu", 16))

grid_layiut = ttk.Frame(root)
grid_layiut.pack(pady=10)

def start():
    pass

def skip():
    pass

def repeat():
    pass

def reset():
    pass


pomodoro_type_label = ttk.Label(grid_layiut, text="work", font=("Ubuntu", 16), background="pink")
pomodoro_type_label.grid(row=1, column=1, sticky="sw")

pomodoro_timer_label = ttk.Label(grid_layiut, text="25:00", font=("Ubuntu", 54), background="pink")
pomodoro_timer_label.grid(row=2, column=1, rowspan=3, sticky="n")

start_button = ttk.Button(grid_layiut, text="Start", command=start)
start_button.grid(row=1, column=0)

skip_button = ttk.Button(grid_layiut, text="Skip", command=reset)
skip_button.grid(row=2, column=0)

repeat_button = ttk.Button(grid_layiut, text="Repeat", command=reset)
repeat_button.grid(row=3, column=0)

reset_button = ttk.Button(grid_layiut, text="Reset", command=reset)
reset_button.grid(row=4, column=0)

pomodoro_counter_label = ttk.Label(grid_layiut, text="Pomodoro: 0:0", font=("Ubuntu", 16))
pomodoro_counter_label.grid(row=5, column=0, columnspan=2)




root.mainloop()