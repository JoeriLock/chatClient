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

    #sets chyper and pub key
    def getKeys(self):
        if(len(sys.argv) > 2):
            cypher = Cypher(sys.argv[1],sys.argv[2])
            if(len(sys.argv) > 3):
                self.pubKey = sys.argv[3]
            return chyper
        #generate keys
        enc = Encryption(79,83)
        print("priv:" + str(enc.private))
        print("pub:" + str(enc.pub))
        print("mod:" + str(enc.n))
        cypher = Cypher(enc.private,enc.n)
        self.pubKey = enc.pub
        return cypher

    def startListen(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen()
        conn, addr = self.s.accept()
        print('Conected by', addr)


        while True:
            try:
                data = conn.recv(1024).decode()
                if(data != ""):
                    print(data)
                if(data == 'need key'):
                    print('Gonna send key to client')
                    print(str(self.pubKey)+","+str(self.cypher.mod))
                    self.sendMessage(str(self.pubKey)+","+str(self.cypher.mod),conn)
                else:
                    value = self.cypher.deChyperList(data.split(","))
                    print(value)
            except socket.error:
                print("Error Occured.")
                break

        conn.close()

    def sendMessage(self,msg,conn):
        conn.sendall(msg.encode())

server = Server('127.0.0.1',5005)
