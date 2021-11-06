import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

red = [(156,43,46),(180,255,255)]
red2 = [(0 , 101 , 122), (179 , 209 , 201)]
red4 = [(2 , 199 , 127), (6 , 234 , 151)]
green = [(35,43,46),(77,255,255)]


squ_x = None
squ_y = None

while cap.isOpened():
     (ret,frame) = cap.read()
     frame = cv2.flip (frame,1)
     frame_img = frame
     # frame_img_bgr = cv2.cvtColor(frame_img, cv2.COLOR_RGB2BGR)  # 将图片转换到BRG空间
     frame_img_hsv = cv2.cvtColor(frame_img, cv2.COLOR_RGB2HSV)  # 将图片转换到HSV空间
     # frame_img = cv2.GaussianBlur(frame_img_hsv, (3, 3), 0)  # 高斯模糊
     frame_img_mask = cv2.inRange(frame_img_hsv, green[0], green[1])  # 二值化
     # frame_img_closed = cv2.erode(frame_img_mask, None, iterations=2)  # 腐蚀
     # frame_img_opened = cv2.dilate(frame_img_mask, np.ones((4, 4), np.uint8), iterations=2)  # 膨胀    先腐蚀后运算等同于开运算
     (contours, hierarchy) = cv2.findContours(frame_img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #CHAIN_APPROX_NONE
     if len(contours) != 0:
          area = []
          for cn in contours:
               contour_area = math.fabs(cv2.contourArea(cn))
               area.append(contour_area)
          max_index = np.argmax(area)
          squ_x, squ_y, w, h = cv2.boundingRect(contours[max_index])
          #cv2.rectangle(frame, (squ_x, squ_y), (squ_x + w, squ_y + h), (153, 153, 0), 5)
          #(squ_x, squ_y), radius = cv2.minEnclosingCircle(contours[max_index])
          # cv2.circle(img, (int(chest_circle_x), int(chest_circle_y)), int(chest_radius), (0, 0, 255))
          print('x=', squ_x, 'y=', squ_y,'宽',w,'高',h)
     #out.write(frame)
     k = cv2.waitKey(5)
     name = 20
     if k == ord("p"):

          cv2.imwrite(".\\demo\\clo"+str(name)+".png",frame)
     sp = frame.shape
     print(sp)
     cv2.imshow('test',frame)
     cv2.waitKey(15)
     # cv2.imshow('test2', frame_img_mask)
     # cv2.waitKey(15)

