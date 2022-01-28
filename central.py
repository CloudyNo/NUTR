from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from threading import Thread as T

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
local_ip_address = s.getsockname()[0]
print("Running Central Communication Server")
print("Your ip   :", local_ip_address)
s.close()

PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname('0.0.0.0')
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
connections = []

def handling(self,c,a):
    while True:
        data = mySocket.recv(SIZE)
        for client in connections:
            client.send(data)
            print(str(a[0])+':',(data.decode('utf-8')[0]))
        
        if not data:
            print(str(a[0])+':',"disconnected")
            self.connections.remove(c)
            c.close()
            break

            