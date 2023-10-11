import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 
import os 


def harrisCorner(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgGray = np.float32(imgGray)

    plt.figure()
    plt.subplot(131)
    plt.imshow(imgGray,cmap='gray')

    plt.subplot(132)
    blockSize = 5 
    sobelSize = 3 
    k = 0.04
    harris = cv.cornerHarris(imgGray,blockSize,sobelSize,k)
    plt.imshow(harris)

    plt.subplot(133)
    imgRGB[harris>0.05*harris.max()] = [255,0,0]
    plt.imshow(imgRGB)

    plt.show() 

if __name__ == '__main__': 
    harrisCorner() 