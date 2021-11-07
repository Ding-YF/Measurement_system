from socket import *
from time import ctime
import threading
import cv2
import numpy as np
import math
from tkinter import Label
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(18, RPi.GPIO.OUT)

HOST = ''  # 169.254.200.85
PORT1 = 8080
PORT2 = 8081
BUFSIZ = 1024

print('11')
url = 'http://169.254.2.14:8080/?action=stream'
url2 = 'http://169.254.37.90:8080/?action=stream'
cap = cv2.VideoCapture(url)
cap2 = cv2.VideoCapture(url2)
print('22')

green = [(35, 43, 46), (77, 255, 255)]


# tcpSvrSock=0
# tcpSvrSock2=0

def tcp1(PORT):  # 第一台设备端口为8080
    global tcpCliSock, addr
    tcpSvrSock = socket(AF_INET, SOCK_STREAM)
    tcpSvrSock.bind((HOST, PORT1))
    tcpSvrSock.listen(5)
    while True:
        print("waiting first for connection !!!")
        tcpCliSock, addr = tcpSvrSock.accept()
        print("connect form", addr)


def tcp2(PORT2):  # 第二台设备端口为8081
    global tcpCliSock2, addr2
    tcpSvrSock2 = socket(AF_INET, SOCK_STREAM)
    tcpSvrSock2.bind((HOST, PORT2))
    tcpSvrSock2.listen(5)
    while True:
        print("waiting second for connection !!!")
        tcpCliSock2, addr2 = tcpSvrSock2.accept()
        print("connect form", addr2)


# 多线程
t1 = threading.Thread(target=tcp1, name="设备一", args=(PORT1,))
t2 = threading.Thread(target=tcp2, name="设备二", args=(PORT2,))
t1.start()
t2.start()


def get_img1():
    while cap.isOpened():
        (ret, frame) = cap.read()
        # frame = cv2.flip(frame, 1)
        frame_img_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)  # 将图片转换到HSV空间
        frame_img_mask = cv2.inRange(frame_img_hsv, green[0], green[1])  # 二值化
        (contours, hierarchy) = cv2.findContours(frame_img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for cn in contours:
                contour_area = math.fabs(cv2.contourArea(cn))
                if (contour_area > 100):
                    x_point, y_point, w, h = cv2.boundingRect(cn)  # contours[cn]
                    cv2.rectangle(frame, (x_point - 20, y_point), (x_point + w + 30, y_point + 355), (153, 153, 0), 5)
        cv2.imshow('frame5', frame)
        cv2.waitKey(15)


# th1 = threading.Thread(target=get_img1)
# th1.setDaemon(True)
# th1.start()

def get_img2():
    while cap2.isOpened():
        (ret, frame) = cap2.read()
        # frame = cv2.flip(frame, 1)
        frame_img_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)  # 将图片转换到HSV空间
        frame_img_mask = cv2.inRange(frame_img_hsv, green[0], green[1])  # 二值化
        (contours, hierarchy) = cv2.findContours(frame_img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for cn in contours:
                contour_area = math.fabs(cv2.contourArea(cn))
                if (contour_area > 100):  # and contour_area < 400
                    x_point, y_point, w, h = cv2.boundingRect(cn)  # contours[cn]
                    cv2.rectangle(frame, (x_point - 20, y_point), (x_point + w + 30, y_point + h + 120), (153, 153, 0),
                                  5)
        cv2.imshow('frame6', frame)
        cv2.waitKey(15)


th2 = threading.Thread(target=get_img2)
th2.setDaemon(True)
th2.start()

while True:
    op = input(">>>")
    if (op == "1"):
        tcpCliSock.send(bytes(op, 'utf-8'))

        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')
        widget = Label(None, text=data)  # 生成
        widget.pack()  # 布置
        widget.mainloop()  # 开始时间循环

        for i in range(0, 10):  # 声光
            RPi.GPIO.output(18, True)
            time.sleep(0.5)
            RPi.GPIO.output(18, False)
            time.sleep(0.5)
        RPi.GPIO.cleanup()

        print('data from ', addr, data)
    elif (op == "2"):
        tcpCliSock2.send(bytes(op, 'utf-8'))
        data = tcpCliSock2.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')

        for i in range(0, 5):  # 声光
            RPi.GPIO.output(18, True)
            time.sleep(0.1)
            RPi.GPIO.output(18, False)
            time.sleep(0.1)
        RPi.GPIO.cleanup()

        widget = Label(None, text=data)  # 生成
        widget.pack()  # 布置
        widget.mainloop(3)  # 开始时间循环

        print('data from ', addr2, data)

tcpCliSock.close()
