#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is debugged by Harden Qiu

容易牵一发而动全身 不要慌张
"""

from numpy import *
from scipy import optimize
import functools
from matplotlib import pyplot as p #, cm, colors

#method_2  = "Fitting Circle"

# Coordinates of the 2D points
# x1 = r_[36, 36, 19, 18, 33, 26,18,20,-22.564] #
# y1 = r_[14, 10, 28, 31, 18, 26,30,32,10.457]  #
#basename = 'arc'

# 质心坐标
# x_m = mean(x) #x y的平均值 #
# y_m = mean(y)  #

# print('x_m=',x_m,'y_m=',y_m)

#修饰器：用于输出反馈
def countcalls(fn):
    "decorator function count function calls "

    @functools.wraps(fn)
    def wrapped(*args):
        wrapped.ncalls +=1
        return fn(*args)

    wrapped.ncalls = 0
    return wrapped

def calc_R(xc, yc):
    global x,y

    return sqrt((x - xc) ** 2 + (y - yc) ** 2) #求半径

@countcalls
def f_2(c):
    Ri = calc_R(*c)
    return Ri - Ri.mean()

def ys(x_p,y_p):
    global x,y
    x = x_p
    y = y_p
    #圆心估计
    x_m = mean(x)
    y_m = mean(y)
    center_estimate = x_m, y_m
    center_2, _ = optimize.leastsq(f_2, center_estimate)  #最小二乘法

    xc_2, yc_2 = center_2
    Ri_2       = calc_R(xc_2, yc_2)
    #拟合圆的半径
    R_2        = Ri_2.mean()
    residu_2   = sum((Ri_2 - R_2)**2)
    residu2_2  = sum((Ri_2**2-R_2**2)**2)
    ncalls_2   = f_2.ncalls
    return R_2

#输出列表
# fmt = '%-22s %10.5f %10.5f %10.5f %10d %10.6f %10.6f %10.2f'
# print (('\n%-22s' +' %10s'*7) % tuple('方法 Xc Yc Rc nb_calls std(Ri) residu residu2'.split()))
# print('-'*(22 +7*(10+1)))
# print(fmt % (method_2 , xc_2 , yc_2 , R_2 , ncalls_2 , Ri_2.std() , residu_2 , residu2_2 ))
# print(ys(x1,y1))

