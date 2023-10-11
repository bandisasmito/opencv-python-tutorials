import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 
import os 

def watershed(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    img = img[900:1300,300:900]
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    _,imgThreshold = cv.threshold(img,120,255,cv.THRESH_BINARY_INV)

    plt.figure()
    plt.subplot(231)
    plt.imshow(img)
    plt.subplot(232)
    plt.imshow(imgThreshold,cmap='gray')

    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv.morphologyEx(imgThreshold,cv.MORPH_DILATE,kernel)
    plt.subplot(233)
    plt.imshow(imgDilate)

    # computes distance from current pixel to nearest 0 pixel
    distTrans = cv.distanceTransform(imgDilate,cv.DIST_L2,5)
    plt.subplot(234)
    plt.imshow(distTrans)

    _,distThresh = cv.threshold(distTrans,15,255,cv.THRESH_BINARY)
    plt.subplot(235)
    plt.imshow(distThresh)

    distThresh = np.uint8(distThresh)
    _,labels = cv.connectedComponents(distThresh)
    plt.subplot(236)
    plt.imshow(labels)

    plt.figure() 
    plt.subplot(121)
    labels = np.int32(labels)
    labels = cv.watershed(imgRGB,labels)
    plt.imshow(labels)

    plt.subplot(122)
    imgRGB[labels==-1] = [255,0,0]
    plt.imshow(imgRGB)


    plt.show()     


if __name__ == '__main__': 
    watershed() 