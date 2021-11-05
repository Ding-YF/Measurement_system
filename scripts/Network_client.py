from socket import *

HOST = '169.254.200.85'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input(">>>")
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
tcpCliSock.close()