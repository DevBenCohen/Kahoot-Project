from Tkinter import *
from Connections import *
from socket import *
import Display
import API
#import random


#questions = ["questions1.txt", "questions2.txt", "questions3.txt"]
#questionire = random.choice(questions)
root = Tk()
app = Display.Server_Display(root)
s_socket = Server_Socket()
q = open("questions1.txt", "r")
client_list = []

while len(client_list) <= 4:
    client = []
    clientsock, serversock, addr, c_username= s_socket.wait_for_connection()
    client.append(clientsock)
    client.append(serversock)
    client.append(addr)
    client.append(c_username)
    client_list.append(client)
    print "Client Added"
    print client
    print client_list

root.mainloop()
