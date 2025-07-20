import random
import time
from tkinter import Tk, Button, DISABLED


def show_symbol(x, y):
    global first
    global previousx, previousy
    buttons[x, y]["text"] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y:
        if buttons[previousx, previousy]["text"] != buttons[x, y]["text"]:
            time.sleep(0.5)
            buttons[previousx, previousy]["text"] = " "
            buttons[x, y]["text"] = " "
        else:
            buttons[previousx, previousy]["command"] = DISABLED
            buttons[x, y]["command"] = DISABLED
        first = True


win = Tk()
win.title("Matchmaker")
win.resizable(width=False, height=False)
first = True
previousx = 0
previousy = 0
buttons = {}
button_symbols = {}
symbols = [
    "\u2702",
    "\u2705",
    "\u2708",
    "\u2709",
    "\u270a",
    "\u270b",
    "\u270c",
    "\u270f",
    "\u2712",
    "\u2714",
    "\u2716",
    "\u2728",
    "\u2702",
    "\u2705",
    "\u2708",
    "\u2709",
    "\u270a",
    "\u270b",
    "\u270c",
    "\u270f",
    "\u2712",
    "\u2714",
    "\u2716",
    "\u2728",
]

random.shuffle(symbols)


for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=10, height=8)
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

win.mainloop()
