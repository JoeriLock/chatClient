import socket

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print('Conected by', addr)
while True:
    try:
        data = conn.recv(1024)
        if not data:
            break

        print ("client says:" + data)
        conn.sendall("servver says:hi")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
