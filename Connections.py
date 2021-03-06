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

def handler(clientsock, serversock, addr, app):
    q = open("questions1.txt", "r")
    app.show_question(q)


class Server_Socket:
    BUFSIZ = 1024
    Client_List = []
    def __init__ (self):
        self.ip = 'localhost'
        self.port = get_free_port()
        API.update("Ben", self.ip, self.port)
        self.ADDR = (self.ip, self.port)
        self.serversock = socket(AF_INET, SOCK_STREAM)
        self.serversock.bind(self.ADDR)
        self.serversock.listen(4)

    def wait_for_connection(self):
        self.clientsock, self.addr = self.serversock.accept()
        self.c_username = self.clientsock.recv(Server_Socket.BUFSIZ)
        Server_Socket.Client_List.append([self.clientsock, self.c_username, 0])
        return self.clientsock


class Client_Sock:
    BUFSIZ = 1024
    def __init__(self):
        self.info = API.get_details("Ben")
        self.HOST = self.info["result"]["ipaddr"]
        self.PORT = self.info["result"]["port"]
        self.ADDR = (self.HOST, self.PORT)
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
        self.tcpCliSock.connect(self.ADDR)
        self.username = raw_input("Enter a username: ")
        self.tcpCliSock.send(self.username)
        print "connected"
