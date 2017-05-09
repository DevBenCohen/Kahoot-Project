from Tkinter import *


class Client_Display:

    def __init__(self, root):
        self.root = root
        self.root.title("Kahoot Client")
        self.Answer1=Button(self.root, text="1", height=5, width=20, font="Arial 14")
        self.Answer1.grid(row=1, column=1, sticky="W")
        self.Answer2=Button(self.root, text="2", height=5, width=20, font="Arial 14")
        self.Answer2.grid(row=1, column=2, sticky="E")
        self.Answer3=Button(self.root, text="3", height=5, width=20,  font="Arial 14")
        self.Answer3.grid(row=2, column=1, sticky="W")
        self.Answer4=Button(self.root, text="4", height=5, width=20,  font="Arial 14")
        self.Answer4.grid(row=2, column=2, sticky="E")

