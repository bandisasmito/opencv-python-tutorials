import cv2 as cv 
import os 
import numpy as np 
import matplotlib.pyplot as plt 


def hsvColorSegmentation(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lowerBound = np.array([0,0,50])
    upperBound = np.array([10,120,100])
    mask = cv.inRange(hsv,lowerBound,upperBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    cv.imshow('mask',mask)
    cv.waitKey(0)

    debug = 1 

if  __name__ == '__main__': 
    hsvColorSegmentation() 