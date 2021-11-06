import cv2
import numpy as np
import math
from time import ctime
from numpy import *
from scipy import optimize
import functools
import threading
from matplotlib import pyplot as p



x_m = None
y_m = None
x_points = []
y_points = []

def countcalls(fn): #修饰函数
    "decorator function count function calls "

    @functools.wraps(fn)
    def wrapped(*args):
        wrapped.ncalls +=1
        return fn(*args)

    wrapped.ncalls = 0
    return wrapped

def calc_R(xc, yc):

    #return sqrt((x_points - xc) ** 2 + (y_points - yc) ** 2) #求半径
    tem = sqrt((x_points - xc) ** 2 + (y_points - yc) ** 2)
    # print('x_points',x_points)
    # print('y_points',y_points)
    # print('xc',xc)
    # print('yc',yc)
    # print('tem',tem)
    return tem

@countcalls
def f_2(c):
    Ri = calc_R(*c)
    return Ri - Ri.mean()

def fitting():
    #圆心估计
    global R_2  #不知道没有提前定义会不会报错
    center_estimate = x_m, y_m
    center_2, _ = optimize.leastsq(f_2, center_estimate)  #最小二乘法

    xc_2, yc_2 = center_2
    Ri_2       = calc_R(xc_2, yc_2)
    #拟合圆的半径
    R_2        = Ri_2.mean()
    residu_2   = sum((Ri_2 - R_2)**2)
    residu2_2  = sum((Ri_2**2-R_2**2)**2)
    ncalls_2   = f_2.ncalls
    print(R_2)
    # print('R_2',R_2)
    #return R_2