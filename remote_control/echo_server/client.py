import socket

host = "192.168.0.9"
port = 8008

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b'Hello, world!')
    data = s.recv(1024)
    print(f'Received: {data}')
