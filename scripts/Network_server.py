from socket import *
from time import ctime
import struct

HOST = ''   #169.254.200.85
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSvrSock = socket(AF_INET,SOCK_STREAM)
tcpSvrSock.bind(ADDR)
tcpSvrSock.listen(5)

while True:
    print("waiting for connection !!!")
    tcpCliSock,addr = tcpSvrSock.accept()
    print("connect form",addr)

    while True:
        #data = tcpCliSock.recv(BUFSIZ)
        fileinfo_size = struct.calcsize('128sq')
        img_recv = tcpCliSock.recv(fileinfo_size)
        if img_recv:
            filename, filesize = struct.unpack('128sq', img_recv)
            fn = filename.decode().strip('\x00')  #去掉不可见的字符 \x00
    tcpCliSock.close()
tcpCliSock.close()