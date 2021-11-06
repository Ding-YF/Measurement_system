import cv2
import numpy as np
import math
from time import ctime

cap = cv2.VideoCapture(1)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

red = [(156,43,46),(180,255,255)]
green = [(35,43,46),(77,255,255)]


squ_x = None
squ_y = None
c = 1
timeF = 8
three_point = []

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

def getCircle(p1, p2, p3):
    x21 = p2[0] - p1[0]
    y21 = p2[1] - p1[1]
    x32 = p3[0] - p2[0]
    y32 = p3[1] - p2[1]
    # three colinear
    if (x21 * y32 - x32 * y21 == 0):
        return None
    xy21 = p2[0] * p2[0] - p1[0] * p1[0] + p2[1] * p2[1] - p1[1] * p1[1]
    xy32 = p3[0] * p3[0] - p2[0] * p2[0] + p3[1] * p3[1] - p2[1] * p2[1]
    y0 = (x32 * xy21 - x21 * xy32) / 2 * (y21 * x32 - y32 * x21)
    x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
    R = ((p1[0] - x0) ** 2 + (p1[1] - y0) ** 2) ** 0.5
    return x0, y0, R

# p1, p2, p3 = Point(0, 0), Point(4, 0), Point(2, 2)
# print(getCircle(p1, p2, p3))


while cap.isOpened():
     (ret,frame) = cap.read()
     frame = cv2.flip (frame,1)
     frame_img = frame
     frame_img_hsv = cv2.cvtColor(frame_img, cv2.COLOR_RGB2HSV)  # 将图片转换到HSV空间
     frame_img_mask = cv2.inRange(frame_img_hsv, green[0], green[1])  # 二值化
     (contours, hierarchy) = cv2.findContours(frame_img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     if len(contours) != 0:
          area = []
          for cn in contours:
               contour_area = math.fabs(cv2.contourArea(cn))
               area.append(contour_area)
          max_index = np.argmax(area)
          # print('max_area=', area[max_index])
          squ_x, squ_y, w, h = cv2.boundingRect(contours[max_index])
     # print('tm1 = ',ctime())
     if len(three_point) < 3:
          if (c%timeF == 0):
               if (area[max_index]>160 and area[max_index]<350):
                    print('-in-')
                    point = [squ_x,squ_y]
                    three_point.append(point)
     else:
          print(three_point)
          x0,y0,R = getCircle(three_point[0],three_point[1],three_point[2])
          print('R=',R)
          break
          print('tm2 = ',ctime())
     c = c + 1
     if (area[max_index]>160 and area[max_index]<350):
          cv2.rectangle(frame, (squ_x, squ_y), (squ_x + w, squ_y + h), (153, 153, 0), 5)
     # print('x=', squ_x, 'y=', squ_y,'宽',w,'高',h)
     cv2.imshow('test', frame)
     cv2.waitKey(15)
     cv2.imshow('test2', frame_img_mask)
     cv2.waitKey(15)
