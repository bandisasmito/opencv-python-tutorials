import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 


def goodCornerDetection(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    maxCorners = 200
    qualityLevel = 0.01  
    minDistance = 20 
    '''
        qualityLevel: 
            qualityMeasure*qualityLevel = acceptableQualityMeasure 
            1500*0.01 = 15 -> less than 15 rejected 
        minDistance: 
            min distance between corners 
        options: 
            shi tomasi (default) or harris corner

        different from bare bones harrisCorners
        also does maximal supression (finding peak in region)

        cornerHarris vs cornerMinEigen
    '''
    corners = cv.goodFeaturesToTrack(imgGray,maxCorners,qualityLevel,minDistance)

    for corner in corners:
        t = 1  
        x = int(corner[0][0])
        y = int(corner[0][1])
        cv.circle(imgRGB,(x,y),10,(255,0,0),-1)

    plt.figure() 
    plt.imshow(imgRGB)
    plt.show() 
    debug = 1 

if __name__ == '__main__': 
    goodCornerDetection() 
    
