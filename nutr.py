#   Network Utilizing Transmitter and Receiver

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from threading import Thread as T
from time import sleep
from os import system, name

PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname('0.0.0.0')
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
local_ip_address = s.getsockname()[0]
print("Your ip   :", local_ip_address)

SERVER_IP = input("Connect to: ")
print()
print("Conversation with", SERVER_IP)

def send():
    while True:
        myMessage = str(input())
        mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

def rec():
    while True:
        data = (mySocket.recvfrom(SIZE))
        print(data[0])

def run():
    p = T(target=rec)
    p2 = T(target=send)
    p.start()
    p2.start()

run()