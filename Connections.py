from socket import *
from Tkinter import *
import thread
import Display
import API

def get_free_port():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port

def handler(clientsock, serversock, addr, app, q):
    score = 0
    currect = app.show_question(q)
    answer = clientsock.recv(1024)
    if data == currect:
        score = score + 10
        print score


class Server_Socket:
    BUFSIZ = 1024
    def __init__ (self):
        self.ip = 'localhost'
        self.port = get_free_port()
        API.update(self.ip, self.port)
        self.ADDR = (self.ip, self.port)
        self.serversock = socket(AF_INET, SOCK_STREAM)
        self.serversock.bind(self.ADDR)
        self.serversock.listen(4)

    def wait_for_connection(self):
        self.clientsock, self.addr = self.serversock.accept()
        self.c_username = self.clientsock.recv(Server_Socket.BUFSIZ)
        return (self.clientsock, self.serversock, self.addr, self.c_username)

class Client_Sock:
    def __init__(self):
        self.info = API.get_details()
        print self.info
