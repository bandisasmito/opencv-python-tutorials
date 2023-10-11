import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

'''
	cv.Feature2D.detect(image[, mask]) ->	keypoints

    https://docs.opencv.org/3.4/d0/d13/classcv_1_1Feature2D.html#a5968e9bc8497a8eb845272b9442559f3

    Fast class is inherited from feature2d class 
'''
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