from socket import *

HOST = '169.254.200.85'
PORT = 8080
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

def transfer():
    pass
while True:
    data = input(">>>")
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
tcpCliSock.close()