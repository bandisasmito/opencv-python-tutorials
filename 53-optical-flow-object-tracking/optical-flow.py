import cv2 as cv 
import numpy as np 
import os 
import matplotlib.pyplot as plt 


def lucasKanade(): 
    # Read image 
    root = os.getcwd() 
    videoPath = os.path.join(root,'demoImages//kayaking.mov')
    videoCapObj = cv.VideoCapture(videoPath)

    # Setup parameters 
    shiTomasiCornerParams = dict(maxCorners=20,
                                 qualityLevel=0.3,
                                 minDistance=50,
                                 blockSize=7 )

    lucasKanadeParams = dict(winSize=(15, 15),
                             maxLevel=2,
                             criteria=(cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT,10,0.03))

    randomColors = np.random.randint(0,255,(100, 3))

    # Find features to track 
    _, frameFirst = videoCapObj.read()
    frameGrayPrev = cv.cvtColor(frameFirst, cv.COLOR_BGR2GRAY)
    cornersPrev = cv.goodFeaturesToTrack(frameGrayPrev, mask=None, **shiTomasiCornerParams)
    mask = np.zeros_like(frameFirst)

    # Loop through each video frame 
    while True: 
        _, frame = videoCapObj.read()
        frameGrayCur = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cornersCur,foundStatus,_ = cv.calcOpticalFlowPyrLK(frameGrayPrev,frameGrayCur,cornersPrev,None, **lucasKanadeParams)

        if cornersCur is not None:
            cornersMatchedCur = cornersCur[foundStatus==1]
            cornersMatchedPrev = cornersPrev[foundStatus==1]

        for i,(curCorner,prevCorner) in enumerate(zip(cornersMatchedCur, cornersMatchedPrev)):
            xCur, yCur = curCorner.ravel()
            xPrev, yPrev = prevCorner.ravel()
            mask = cv.line(mask,(int(xCur),int(yCur)),(int(xPrev),int(yPrev)),randomColors[i].tolist(),2)
            frame = cv.circle(frame, (int(xCur), int(yCur)),5,randomColors[i].tolist(),-1)
            img = cv.add(frame,mask)

        cv.imshow('Video',img)
        cv.waitKey(15)
        frameGrayPrev = frameGrayCur.copy()
        cornersPrev = cornersMatchedCur.reshape(-1,1,2)

def denseOpticalFlow():
    # Read image  
    root = os.getcwd() 
    videoPath = os.path.join(root,'demoImages//kayaking.mov')
    videoCapObj = cv.VideoCapture(videoPath)

    # Prepare HSV image 
    _, frameFirst = videoCapObj.read()
    imgPrev = cv.cvtColor(frameFirst, cv.COLOR_BGR2GRAY)
    imgHSV = np.zeros_like(frameFirst)
    imgHSV[:,:,1] = 255

    # Loop through each video frame 
    while True:
        _, frameCur = videoCapObj.read()
        imgCur = cv.cvtColor(frameCur, cv.COLOR_BGR2GRAY)
        flow = cv.calcOpticalFlowFarneback(prev=imgPrev,next=imgCur,flow=None,pyr_scale=0.5,levels=3,winsize=15,iterations=3,poly_n=5,poly_sigma=1.2,flags=cv.OPTFLOW_FARNEBACK_GAUSSIAN)
        mag,ang = cv.cartToPolar(flow[:,:,0], flow[:,:,1])
        # OpenCV H is [0,180] so divide by 2 
        imgHSV[:,:,0] = ang*180/np.pi/2 
        imgHSV[:,:,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
        imgBGR = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
        cv.imshow('Video', imgBGR)
        cv.waitKey(15) 
        imgPrev = imgCur

if __name__ == '__main__': 
    # lucasKanade()
    denseOpticalFlow()