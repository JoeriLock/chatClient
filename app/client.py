import socket
import sys
from cypher import Cypher
import time


class Client:

    host = "127.0.0.1"
    port = "5005"
    s = ""
    isKeySet = True
    pubKeyFile = './pubkey.txt'

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.cypher = self.getKey()

        self.connect()

    def startConversation(self):
        while True:
            msg = input(":")
            if msg == 'exit':
                break
            enc = self.cypher.chyperString(msg)
            print(enc)
            self.s.sendall(enc.encode())


    def getKey(self):
        if(len(sys.argv) > 2):
            return Cypher(sys.argv[1],sys.argv[2])
        self.isKeySet = False

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        if not self.isKeySet:
            self.s.sendall('need key'.encode())
            data = self.s.recv(1024).decode()
            keys = data.split(',')
            self.cypher = Cypher(keys[0],keys[1])
            self.isKeySet = True
            print(keys)
        self.startConversation()
        self.s.close();


client = Client("127.0.0.1",5005)
