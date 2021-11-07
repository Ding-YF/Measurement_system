from socket import *
from time import ctime
import threading

HOST = ''   #169.254.200.85
PORT1 = 8080
PORT2=8081
BUFSIZ = 1024



def tcp1(PORT): #第一台设备端口为8080
    tcpSvrSock = socket(AF_INET, SOCK_STREAM)
    tcpSvrSock.bind((HOST,PORT))
    tcpSvrSock.listen(5)
    while True:
        print("waiting first for connection !!!")
        tcpCliSock,addr = tcpSvrSock.accept()
        print("connect form",addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            data = data.decode('utf-8')
            # print('data from ',addr,data )
        tcpCliSock.close()

def tcp2(PORT2): #第二台设备端口为8081
    tcpSvrSock2 = socket(AF_INET, SOCK_STREAM)
    tcpSvrSock2.bind((HOST,PORT2))
    tcpSvrSock2.listen(5)
    while True:
        print("waiting second for connection !!!")
        tcpCliSock2,addr = tcpSvrSock2.accept()
        print("connect form",addr)
        while True:
            data2 = tcpCliSock2.recv(BUFSIZ)
            if not data2:
                break
            data2 = data2.decode('utf-8')
            # print('data2 from ',addr ,data2)
        tcpCliSock2.close()

#多线程
t1=threading.Thread(target=tcp1,name="设备一",args=(PORT1,))
t2=threading.Thread(target=tcp2,name="设备二",args=(PORT2,))
t1.start()
t2.start()

if __name__ == '__main__':
    pass