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

