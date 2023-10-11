import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


def FAST(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    imgGray = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    fast = cv.FastFeatureDetector_create()
    minIntensityDiff = 100 
    fast.setThreshold(minIntensityDiff)
    keypoints = fast.detect(imgGray)
    imgGray = cv.drawKeypoints(imgGray,keypoints,imgGray,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    plt.figure()
    plt.imshow(imgGray)
    plt.show() 

if __name__ == '__main__': 
    FAST() 