from socket import *
from time import ctime
import threading

HOST = ''   #169.254.200.85
PORT1 = 8080
PORT2=8081
BUFSIZ = 1024

# tcpSvrSock=0
# tcpSvrSock2=0

def tcp1(PORT): #第一台设备端口为8080
    global tcpCliSock,addr
    tcpSvrSock = socket(AF_INET, SOCK_STREAM)
    tcpSvrSock.bind((HOST,PORT))
    tcpSvrSock.listen(5)
    while True:
        print("waiting first for connection !!!")
        tcpCliSock,addr = tcpSvrSock.accept()
        print("connect form",addr)


def tcp2(PORT2): #第二台设备端口为8081
    global tcpCliSock2,addr2
    tcpSvrSock2 = socket(AF_INET, SOCK_STREAM)
    tcpSvrSock2.bind((HOST,PORT2))
    tcpSvrSock2.listen(5)
    while True:
        print("waiting second for connection !!!")
        tcpCliSock2,addr2 = tcpSvrSock2.accept()
        print("connect form",addr2)


#多线程
t1=threading.Thread(target=tcp1,name="设备一",args=(PORT1,))
t2=threading.Thread(target=tcp2,name="设备二",args=(PORT2,))
t1.start()
t2.start()



while True:
    op = input(">>>")
    if(op=="1"):
        tcpCliSock.send(bytes(op, 'utf-8'))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')
        print('data from ', addr, data)
    elif(op=="2"):
        tcpCliSock2.send(bytes(op, 'utf-8'))
        data = tcpCliSock2.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')
        print('data from ', addr2, data)

tcpCliSock.close()