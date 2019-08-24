from tkinter import *
from tkinter import ttk


class App():
    def __init__(self, master):
        self.master = master
        self.init_widgets()
        self.expr = None

    def init_widgets(self):
        self.show = Label(self.master, relief=SUNKEN, font=('Courier New', 24), width=25, background='white', anchor=E)
        self.show.pack(side=TOP, pady=10)
        p = ttk.Frame(self.master)
        p.pack(side=TOP)
        names = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "=")
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)
            b.bind('<Button-1>', self.click)
            if b['text'] == '=': b.bind('<Double-1>', self.clear)

    def click(self, event):
        if event.widget['text'] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif event.widget['text'] in ("+", "-", "*", "/"):
            if self.expr is None:
                self.expr = self.show['text'] + event.widget['text']
            else:
                self.expr = self.expr + self.show['text'] + event.widget['text']
            self.show['text'] = ''
        elif event.widget['text'] == '=' and self.expr is not None:
            self.expr = self.expr + self.show['text']
            self.show['text'] = str(eval(self.expr))
            self.expr = None

    def clear(self):
        self.expr = None
        self.show['text'] = ''


root = Tk()
root.title("计算器")
App(root)
root.mainloop()
