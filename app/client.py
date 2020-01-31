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
        if not self.isKeySet:
            self.s.sendall('need key'.encode())
            data = self.s.recv(1024).decode()
            self.s.close()
            keys = data.split(',')
            self.cypher = Cypher(keys[0],keys[1])
            self.isKeySet = True



client = Client("127.0.0.1",5005)
