# Server know the private/decryption key
# Gives pub key to anyone who wants it
# Does not send messages, only recievs it

import socket
import sys
from cypher import Cypher
from encryption import Encryption

class Server:
    host = '127.0.0.1'
    port = 5005
    s = ''
    pubKey = ""
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.cypher = self.getKeys()
        self.startListen()

    def getKeys(self):
        if(len(sys.argv) > 2):
            cypher = Cypher(sys.argv[1],sys.argv[2])
            if(len(sys.argv) > 3):
                self.pubKey = sys.argv[3]
            return chyper
        #generate keys
        enc = Encryption(11,81)
        cypher = Cypher(enc.private,enc.n)
        self.pubKey = enc.pub
        return cypher

    def startListen(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        conn, addr = self.s.accept()
        print('Conected by', addr)

        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break

                if(data.decode() == 'need key'):
                    print('Gonna send key to client')
                    self.sendMessage(str(self.pubKey)+","+str(self.cypher.mod),conn)

            except socket.error:
                print("Error Occured.")
                break

        conn.close()

    def sendMessage(self,msg,conn):
        conn.sendall(msg.encode())

server = Server('127.0.0.1',5005)
