from tkinter.ttk import Button, Style

from constants import *


class MyButton(Button):
    def __init__(self, master, text="Button", font=BUTTON_FONT, command=None, fg=FG_BUTTON, bg=BG_BUTTON):
        Style().configure('TButton', font=font, foreground=fg, background=bg, relife="sunken")
        super().__init__(master=master, text=text, command=command)

    def position(self, x, y, height=CONST_HEIGHT, width=BUTTON_WIDTH, anchor=BUTTON_ANCHOR):
        self.place(x=x, y=y, height=height, width=width, anchor=anchor)
