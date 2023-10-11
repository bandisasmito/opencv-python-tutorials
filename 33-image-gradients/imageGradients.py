import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 
import os 

def imageGradients(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)
    # img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure() 
    plt.subplot(221)
    plt.imshow(img)

    laplacian = cv.Laplacian(img,cv.CV_64F,ksize=21)
    # _,laplacian = cv.threshold(laplacian,0,255,cv.THRESH_BINARY)
    plt.subplot(222)
    plt.imshow(laplacian,cmap='gray')

    kx,ky = cv.getDerivKernels(1,0,3)
    print(ky@kx.T)
    sobelX = cv.Sobel(img,cv.CV_64F,1,0,ksize=21)
    # _,sobelX = cv.threshold(sobelX,0,255,cv.THRESH_BINARY)
    plt.subplot(223)
    plt.imshow(sobelX,cmap='gray')

    kx,ky = cv.getDerivKernels(0,1,3)
    print(ky@kx.T)
    sobelY = cv.Sobel(img,cv.CV_64F,0,1,ksize=21)
    # _,sobelY = cv.threshold(sobelY,0,255,cv.THRESH_BINARY)
    plt.subplot(224)
    plt.imshow(sobelY,cmap='gray')


    plt.show() 

if __name__ == '__main__': 
    imageGradients() 