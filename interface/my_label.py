from tkinter.ttk import Label

from constants import *


class MyLabel(Label):
    def __init__(self, master, text="", font=LABEL_FONT, fg=FG_COLOR, bg=BG_COLOR, justify=LABEL_JUSTIFY, width=None,
                 relief=None, wrap=False, wraplength=485):
        super().__init__(master=master, text=text, justify=justify, foreground=fg, background=bg, font=font,
                         width=width, relief=relief)
        if wrap:
            self.configure(wraplength=wraplength)

    def updateText(self, text):
        self.config(text=text)

    def position(self, x, y, height=CONST_HEIGHT, width=LABEL_WIDTH, anchor=LABEL_ANCHOR):
        self.place(x=x, y=y, height=height, width=width, anchor=anchor)
