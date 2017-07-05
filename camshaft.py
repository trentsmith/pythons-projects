import numpy as np
import cv2
import matplotlib.pyplot as plt
import Tkinter as tk
cap = cv2.VideoCapture(0)
r=250
h=90
c=400
w=125  # simply hardcoded the values
track_window = (c,r,w,h)
x = 50
y = 40
while(True):
    ret, frame = cap.read()
    roi = frame[0:100,0:100]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array((50., 50.,50.)), np.array((255.,255.,255.)))
    cv2.circle(mask,(x,y), 63,(0,0,255), -1)
    cv2.imshow('frame',mask)
    iar = np.asarray(mask)
    i =0
   #'''while i<len(mask):
    #    j=0
     #   while j<len(mask[i]):
      #      j=j+1
      #  i=i+1'''
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    if (cv2.waitKey(1) & 0xFF == ord('a')):
        x = x-10
    if (cv2.waitKey(1) & 0xFF == ord('s')):
        y = y-10
    if (cv2.waitKey(1) & 0xFF == ord('d')):
        x = x+10
    if (cv2.waitKey(1) & 0xFF == ord('w')):
        y = y+10
cap.release()
cv2.destroyAllWindows()
