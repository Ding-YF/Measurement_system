from socket import *
import cv2
import struct

HOST = '169.254.200.85'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

cap = cv2.VideoCapture(0)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while cap.isOpened():
    (ret,frame) = cap.read()
    #data = input(">>>")
    img = frame
    img_pack = struct.pack(b'128sq', bytes(img, encoding='utf-8')) #os.stat(filepath).st_size 读取文件大小
    tcpCliSock.send(img_pack)
    #data = tcpCliSock.recv(BUFSIZ)
    #print(data.decode('utf-8'))
    cv2.imshow('test', frame)
    cv2.waitKey(15)
tcpCliSock.close()