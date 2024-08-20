from sys import version_info
from tkinter import *
from tkinter import font as tkFont, ttk
import time
import math
import random
from main import main

main_window = Tk()
big_frame = Frame(main_window)
main_window.title("CharacterAI-RT_Sim alpha v0.2")

start = Button(main_window, text="Начать диалог", command=main, width=30)
start.grid(column=0, row=1)

# label_widget_1 = tk.Label(main_window,
#                           text="ULTIMATE 'MASK OF MADNESS' CLICKER",
#                           height=3,
#                           width=50,
#                           font=("Comic Sans MS", 20),
#                           fg="orange")
#
# label_widget_1.grid(column=0, row=0)

main_window.geometry('1200x480')
main_window.minsize(1200, 480)
main_window.mainloop()

#TODO: почему примитивная эта хуйня не работает
