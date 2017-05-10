from Tkinter import *
#import random

class Client_Display:

    def __init__(self, root):
        self.root = root
        self.root.title("Kahoot Client")
        self.request_username = Label(self.root, text="Enter a username: ", font="Arial 14")
        self.request_username.grid(row=1, column=1, sticky="WS")
        self.username = Entry(self.root, font="Arial 14")
        self.username.grid(row=2,column=1, sticky="W")
        self.send_user = Button(self.root, text="Join the game!", font="Arial 14", command=self.Get_Username)
        self.send_user.grid(row=3,column=2, sticky="E")

    def Answers_Screen(self):
        self.root.geometry("900x472")
        self.Answer1=Button(self.root, text="1", height=10, width=40, font="Arial 14", bg="red")
        self.Answer1.grid(row=1, column=1, sticky="W")
        self.Answer2=Button(self.root, text="2", height=10, width=40, font="Arial 14", bg="blue")
        self.Answer2.grid(row=1, column=2, sticky="E")
        self.Answer3=Button(self.root, text="3", height=10, width=40,  font="Arial 14", bg="orange")
        self.Answer3.grid(row=2, column=1, sticky="W")
        self.Answer4=Button(self.root, text="4", height=10, width=40,  font="Arial 14", bg="green")
        self.Answer4.grid(row=2, column=2, sticky="E")

    def Get_Username(self):
        self.request_username.grid_forget()
        self.username.grid_forget()
        self.send_user.grid_forget()
        self.Answers_Screen(self.root)


class Server_Display:

    def __init__(self, root):
        self.root = root
        self.root.title("Kahoot Server")
        self.root.geometry("975x533")
        self.current_users = Label(self.root, text="Current Users: ", font="Arial 14")
        self.current_users.grid(row=1, column=1, sticky="W")

    def show_question(self, q):
        #questions = ["questions1.txt", "questions2.txt", "questions3.txt"]
        #questionire = random.choice(questions)
        #q = open("questions1.txt", "r")
        self.current_users.grid_forget()
        ques = q.readline()
        self.Question = Label(self.root, text = ques, font="Arial 22")
        self.Question.grid(row=1, column=1, sticky="E")
        ans1 = q.readline()
        self.Option1 = Label(self.root, text = ans1, height=7, width=30, font="Arial 20", bg="red")
        self.Option1.grid(row=2, column=1, sticky="W")
        ans2 = q.readline()
        self.Option2 = Label(self.root, text = ans2, height=7, width=30, font="Arial 20", bg="blue")
        self.Option2.grid(row=2, column=2, sticky="E")
        ans3 = q.readline()
        self.Option3 = Label(self.root, text = ans3, height=7, width=30, font="Arial 20", bg="orange")
        self.Option3.grid(row=3, column=1, sticky="W")
        ans4 = q.readline()
        self.Option4 = Label(self.root, text = ans4, height=7, width=30, font="Arial 20", bg="green")
        self.Option4.grid(row=3, column=2, sticky="E")
        currect = q.readline()
