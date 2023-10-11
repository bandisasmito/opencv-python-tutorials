import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv
import os 

def objectTracking(option):
    # Read Image
    root = os.getcwd() 
    videoPath = os.path.join(root,'demoImages//kayaking.mov')
    videoCapObj = cv.VideoCapture(videoPath)
    _,frame = videoCapObj.read()

    # Plot first frame of video 
    plt.figure() 
    plt.subplot(211)
    plt.imshow(frame)

    # Extract region for tracking 
    xTopLeft = 350 
    yTopLeft = 760 
    w = 85
    h = 40 
    windowTracker = (xTopLeft,yTopLeft,w,h)
    imgRegion = frame[yTopLeft:yTopLeft+h,xTopLeft:xTopLeft+w]
    plt.subplot(212)
    plt.imshow(imgRegion)
    plt.show() 

    # Set range to track based on hsv colors 
    hsvImgRegion = cv.cvtColor(imgRegion,cv.COLOR_BGR2HSV)
    hsvLowerLimit = np.array([18/360*2, 200, 0])
    hsvUpperLimit = np.array([22/360*2, 255, 255])
    mask = cv.inRange(hsvImgRegion,hsvLowerLimit,hsvUpperLimit)
    histImgRegion = cv.calcHist([hsvImgRegion],[0],mask,[180],[0,180])
    cv.normalize(histImgRegion,histImgRegion,0,255,cv.NORM_MINMAX) 
    termCrit = (cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT,10,1)
    color =  (144, 238, 144)
    
    # Loop through each frame and track object 
    while True:
        ret, videoFrame = videoCapObj.read()
        if ret == True:
            hsv = cv.cvtColor(videoFrame,cv.COLOR_BGR2HSV)
            imgBackProj = cv.calcBackProject([hsv],[0],histImgRegion,[0,180],1)

        if option == 'meanshift': 
            _,windowTracker = cv.meanShift(imgBackProj,windowTracker,termCrit)
            xTopLeft,yTopLeft,w,h = windowTracker
            videoFrame = cv.rectangle(videoFrame,(xTopLeft,yTopLeft),(xTopLeft+w,yTopLeft+h),color,2)

        if option == 'camshift':
            ret, windowTracker = cv.CamShift(imgBackProj,windowTracker,termCrit)
            boxPts = cv.boxPoints(ret)
            videoFrame = cv.polylines(videoFrame,[np.int32(boxPts)],True,color,2)

        cv.imshow('video',videoFrame)
        cv.waitKey(15)

if __name__ == '__main__': 
    # objectTracking(option='meanshift') 
    objectTracking(option='camshift') 