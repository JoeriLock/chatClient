# Server know the private/decryption key
# Gives pub key to anyone who wants it
# Does not send messages, only recievs it

import socket

class Server:
    host = '127.0.0.1'
    port = 5005
    s = ''
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.startListen()

    def startListen(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        conn, addr = self.s.accept()
        print('Conected by', addr)
        self.sendMessage("123",conn)

        # while True:
        #     try:
        #         data = conn.recv(1024)
        #         if not data:
        #             break
        #
        #         print ("client says:")
        #         print(data)
        #         self.sendMessage("server says:hi", conn)
        #
        #     except socket.error:
        #         print("Error Occured.")
        #         break

        conn.close()

    def sendMessage(self,msg,conn):
        conn.sendall(msg.encode())

server = Server('127.0.0.1',5005)
