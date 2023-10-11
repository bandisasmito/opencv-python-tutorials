import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

def morphTrans():
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    imgGray = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    maxValue = 255 
    blocksize = 7 
    offsetC = 3 

    plt.subplot(241)
    imgGaus = cv.adaptiveThreshold(imgGray,maxValue,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,blocksize,offsetC)
    imgGaus = cv.GaussianBlur(imgGaus,(7,7),sigmaX=2)
    plt.imshow(imgGaus,cmap='gray')
    plt.title('gaus thres')

    kernel = np.ones((7,7),np.uint8)
    erosion = cv.erode(imgGaus,kernel,iterations=1)
    plt.subplot(242)
    plt.imshow(erosion,cmap='gray')
    plt.title('erosion')

    dilation = cv.dilate(imgGaus,kernel,iterations=1)
    plt.subplot(243)
    plt.imshow(dilation,cmap='gray')
    plt.title('dilation')


    morphTypes = [cv.MORPH_OPEN, 
                  cv.MORPH_CLOSE,
                  cv.MORPH_GRADIENT,
                  cv.MORPH_TOPHAT,
                  cv.MORPH_BLACKHAT]
    morphTitles = ['open','close','gradient','tophat','blackhat']

    for i in range(len(morphTypes)): 
        plt.subplot(2,4,i+4)
        plt.imshow(cv.morphologyEx(imgGaus,morphTypes[i],kernel),cmap='gray')
        plt.title(morphTitles[i])

    plt.show() 

    ellipseKernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    crossKernel = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
    print(ellipseKernel)
    print(crossKernel)


if __name__ == '__main__': 
    morphTrans() 