from socket import *

def get_free_port():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port

class Server_Socket:

    def __init__(self):
        
