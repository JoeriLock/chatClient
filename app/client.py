import socket

class Client:

    host = ""
    port = ""
    s = ""

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.s.sendall(b'Hello wolrd')
        data = self.s.recv(1024)
        self.s.close()
        print('Received', repr(data))

client = Client("127.0.0.1",5005)
