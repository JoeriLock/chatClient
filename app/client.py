import socket
import sys
from cypher import Cypher

class Client:

    host = ""
    port = ""
    s = ""
    isKeySet = True
    pubKeyFile = './pubkey.txt'

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.cypher = self.getKey()
        self.connect()

    def getKey(self):
        if(len(sys.argv) > 2):
            return Cypher(sys.argv[1],sys.arv[2])
        self.isKeySet = False

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.s.sendall('need key'.encode())
        data = self.s.recv(1024)
        self.s.close()
        print('Received', repr(data))

client = Client("127.0.0.1",5005)
