#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

import cv2
import numpy as np
import math
import time
from time import ctime
from numpy import *
from scipy import optimize
import functools
import threading
from socket import *
from matplotlib import pyplot as p

import double_multi as dm

#输出log
# import sys
# f_handler=open('out.log', 'w')
# sys.stdout=f_handler

cap = cv2.VideoCapture('http://169.254.2.14:8080/?action=stream')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


red = [(156,43,46),(180,255,255)]
green = [(35,43,46),(77,255,255)]

frame_img = None
tcpCliSock = None
x_points = []
y_points = []
x_pointss = [36, 36, 19, 18, 33, 26,18,20,-22.564]
y_pointss = [14, 10, 28, 31, 18, 26,30,32,10.457]
c = 1
timeF = 8

HOST = '169.254.211.43'
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 1024

def get_img():
    global frame_img
    while cap.isOpened():
        # print('--1111--')
        (ret,frame) = cap.read()
        frame = cv2.flip (frame,1)
        frame_img = frame
        # cv2.imshow('test', frame_img)
        # cv2.waitKey(15)
th1 = threading.Thread(target=get_img)
th1.setDaemon(True)
th1.start()

def find_point(img):
    global x_points , y_points , x_m ,y_m
    frame_img_hsv = cv2.cvtColor(frame_img, cv2.COLOR_RGB2HSV)  # 将图片转换到HSV空间
    frame_img_mask = cv2.inRange(frame_img_hsv, green[0], green[1])  # 二值化
    (contours, hierarchy) = cv2.findContours(frame_img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('-55-')
    if len(contours) != 0:
        for cn in contours:
            # print('-66-')
            contour_area = math.fabs(cv2.contourArea(cn))
            # if (contour_area>160 and contour_area < 350):
            if (contour_area > 100):
                print('-777-')
                # print(cn)   ####程序到这里报错，因为cn是个轮廓
                x_point, y_point, w, h = cv2.boundingRect(cn) #contours[cn]
                # if (contour_area > 100 and contour_area < 400):
                #     cv2.rectangle(frame, (x_point, y_point), (x_point + w, y_point + h), (153, 153, 0), 5)
                x_points.append(x_point)
                y_points.append(y_point)
                x_m = mean(x_points)
                y_m = mean(y_points)
def client(ADDR):
    global tcpCliSock
    print('--444--')
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    print('--555--')
    tcpCliSock.connect(ADDR)
    print('connect to',ADDR)
th2=threading.Thread(target=client,name="设备一",args=(ADDR,))
th2.setDaemon(True)
th2.start()

if __name__ == '__main__':
    key = 0
    while True:
        if frame_img is None:
            print('init')
            time.sleep(0.3)
        elif (key == 1):
            print('--in 1--')
            # R = 30
            # time.sleep(3)
            # if tcpCliSock is not None:
            #     print('--222--')
            #     tcpCliSock.send(bytes(str(R), 'utf-8'))
            # print(R)
    ######################## for test ##########################
            find_point(frame_img)
            print(12222)
            if len(x_points) == 400:
                print(13333)
                R = dm.ys(x_points,y_points)
                R = R + 242
                R = R * 0.061972
                if tcpCliSock is not None:
                    tcpCliSock.send(bytes(str(R), 'utf-8'))
                x_points = []
                y_points = []
                print(R)
                key+=1
        else:
            print('wait')
            key = tcpCliSock.recv(BUFSIZE)
            key = int(key)
            time.sleep(0.5)
            continue
