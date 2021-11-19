#   Network Utilizing Transmitter and Receiver

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from threading import Thread as T

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
local_ip_address = s.getsockname()[0]
print("Your ip   :", local_ip_address)
s.close()

PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname('0.0.0.0')
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

SERVER_IP = input("Connect to: ")

def send():
    while True:
        myMessage = str(input())
        mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

def rec():
    while True:
        data = (mySocket.recvfrom(SIZE)[0])
        print(data.decode('utf8'))

def run():
    p = T(target=rec)
    p2 = T(target=send)
    p3 = T(target=recping)
    p.start()
    p2.start()
    p3.start()

def sping():
    for i in range(3):
        mySocket.sendto(("ping").encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        if (mySocket.recvfrom(SIZE)[0]).decode('utf-8') == "ping":
            print(i)
            return i

def recping():
    while True:
        if (mySocket.recvfrom(SIZE)[0]).decode('utf-8') == "ping":
            dar = (mySocket.recvfrom(SIZE)[1]).decode('utf-8')
            mySocket.sendto(("ping").encode('utf-8'),(dar))

sping()
run()