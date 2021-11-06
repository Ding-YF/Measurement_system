from socket import *
from time import ctime

HOST = ''   #169.254.200.85
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSvrSock = socket(AF_INET,SOCK_STREAM)
tcpSvrSock.bind(ADDR)
tcpSvrSock.listen(5)

while True:
    ret = True
    print("waiting for connection !!!")
    tcpCliSock,addr = tcpSvrSock.accept()
    print("connect form",addr)
    while ret:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')
        print(data)
        ret = False
    tcpCliSock.close()
    print('tcp out')
tcpCliSock.close()