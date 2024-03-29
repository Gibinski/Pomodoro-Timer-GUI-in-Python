import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage
import pygame


class PomodoroTimer:
    
    def __init__(self):
        pygame.mixer.init()# initialise the pygame
  
        self.root = tk.Tk()
        self.root.geometry("460x300")
        self.root.title("Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="tomato.png"))
        self.root["bg"] = "#333"

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubintu", 16))
        self.s.configure("TButton", font=("Ubintu", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short break")
        self.tabs.add(self.tab3, text="Long break")

        self.pomodoro_timer_label = ttk.Label(self.tab1, text="work 25:00", font=("Ubuntu", 64), background="indian red")
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(self.tab2, text="break 05:00", font=("Ubuntu", 64), background="yellow")
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(self.tab3, text="rest 20:00", font=("Ubuntu", 64), background="light green")
        self.long_break_timer_label.pack(pady=20)

        self.grid_layiut = ttk.Frame(self.root)
        self.grid_layiut.pack(pady=10)
        
        self.start_button = ttk.Button(self.grid_layiut, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layiut, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)
        
        self.reset_button = ttk.Button(self.grid_layiut, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)
        
        self.pomodoro_counter_label = ttk.Label(self.grid_layiut, text="Pomodoro: 0", font=("Ubuntu", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3)

        self.pomodoros = 0
        self.long_break_counter = True
        self.skipped = False
        self.stopped = False
        self.running = False

        self.root.mainloop()
    
    def play(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=0)

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            self.play("work.mp3")
            full_seconds = 60 * 25
            while full_seconds > 1 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.config(text=f"work {minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoeos: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                self.start_timer()
        elif timer_id == 2:
            self.play("break.mp3")
            full_seconds = 60 * 5
            while full_seconds > 1 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(text=f"break {minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        elif timer_id == 3:
            self.play("rest.mp3")
            full_seconds = 0
            if self.long_break_counter:
                full_seconds = 60 * 20
                self.long_break_timer_label.config(text=f"rest 20:00", background="light green")
                self.long_break_counter = False
            else:
                full_seconds = 60 * 50
                self.long_break_timer_label.config(text=f"rest 50:00", background="cyan")
                self.long_break_counter = True  
            while full_seconds > 1 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(text=f"rest {minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        else:
            print("Invalid timer id")

    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.pomodoro_timer_label.config(text=f"work 25:00")
        self.short_break_timer_label.config(text=f"bewak 05:00")
        self.long_break_timer_label.config(text=f"rest 20:00")
        self.pomodoro_counter_label.config(text=f"Pomodoeos: 0")
        self.running = False

    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text=f"work 25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text=f"break 05:00")
        elif current_tab == 2:
            if self.long_break_counter:
                self.long_break_timer_label.config(text=f"rest 20:00")
            else:
                self.long_break_timer_label.config(text=f"rest 50:00")

        self.skipped = True
        self.stopped = True

        
PomodoroTimer()
