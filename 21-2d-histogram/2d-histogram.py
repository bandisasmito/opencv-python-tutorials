import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np 

def histogram2d():

    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
    plt.figure()
    plt.subplot(131)
    plt.imshow(imgRGB)

    plt.subplot(132)
    plt.imshow(hist)
    plt.ylabel('hue')
    plt.xlabel('saturation')


    lowerBound = np.array([106,128,0])
    upperBound = np.array([112,200,255])
    mask = cv.inRange(hsv,lowerBound,upperBound)

    plt.subplot(133)
    plt.imshow(mask,cmap='gray')
    plt.show()

if __name__ == '__main__':
   histogram2d()