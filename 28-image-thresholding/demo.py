import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

def thresholding(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\tesla.jpg')
    img = cv.imread(imgPath)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    hist = cv.calcHist([imgGray], [0], None, [256], [0,256])
    plt.figure() 
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.show() 

    thresOpt = [cv.THRESH_BINARY, 
                cv.THRESH_BINARY_INV,
                cv.THRESH_TOZERO,
                cv.THRESH_TOZERO_INV,
                cv.THRESH_TRUNC]
    
    thresNames = ['binary','binaryInv','toZero','toZeroInv','trunc']

    plt.figure() 
    plt.subplot(231)
    plt.imshow(imgGray,cmap='gray')

    for i in range(len(thresOpt)): 
        plt.subplot(2,3,i+2)
        _, imgThres = cv.threshold(imgGray,70,255,thresOpt[i])
        plt.imshow(imgThres,cmap='gray') 
        plt.title(thresNames[i])

    plt.show() 

if __name__ == '__main__': 
    thresholding() 