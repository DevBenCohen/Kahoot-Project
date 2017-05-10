from Tkinter import *
import Display
#import random

#questions = ["questions1.txt", "questions2.txt", "questions3.txt"]
#questionire = random.choice(questions)
q = open("questions1.txt", "r")
root = Tk()h
app = Display.Server_Display(root)
app.show_question(q)
app.show_question(q)
root.mainloop()
