import socket

host = ''
port = 5005
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

        print ("client says:")
        print(data)
        conn.sendall("server says:hi".encode())

    except socket.error:
        print("Error Occured.")
        break

conn.close()
