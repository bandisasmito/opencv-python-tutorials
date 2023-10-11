# pip install opencv-contrib-python==3.4.2.16
# python 3.6.8 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


def SURF():
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    imgGray = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    hessianThreshold = 3000
    surf = cv.xfeatures2d.SURF_create(hessianThreshold)
    keypoints = surf.detect(imgGray,None)
    imgGray = cv.drawKeypoints(imgGray,keypoints,imgGray,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    plt.figure()
    plt.imshow(imgGray)
    plt.show() 

if __name__ == '__main__': 
    SURF() 
