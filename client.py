import socket

host = socket.gethostname()
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello wolrd')
data = s.recv(1024)
s.close()
print('Received', repr(data))



print(str(host))
