import socket

class Server:
    def __init__(self, port,host='192.168.0.38'):
        self.port = port
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def run(self):
        self.s.bind((self.host,self.port))
        self.s.listen(5)
        print(f'listening on {self.port}')

        while True:
            c,addr = self.s.accept()
            msg = c.recvmsg(1024)
            print(f'received: {msg[0].decode("utf-8")}')
            reply = b'server received'
            
            c.sendall(reply)

if __name__ == "__main__":
    server = Server(8008)
    server.run()
