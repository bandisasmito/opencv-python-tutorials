import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def pureColors(): 
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((zeros,zeros,255*ones))
    gImg = cv.merge((zeros,255*ones,zeros))
    rImg = cv.merge((255*ones,zeros,zeros))
    blackImg = cv.merge((zeros,zeros,zeros))
    whiteImg = cv.merge((255*ones,255*ones,255*ones))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('blue')
    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('green')
    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('red')
    plt.subplot(234)
    plt.imshow(blackImg)
    plt.title('black')
    plt.subplot(235)
    plt.imshow(whiteImg)
    plt.title('white')

    plt.show() 

def bgrChannelGrayscale(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    b,g,r = cv.split(img) 

    plt.figure() 
    plt.subplot(131)
    plt.imshow(b,cmap='gray')
    plt.title('b')
    plt.subplot(132)
    plt.imshow(g,cmap='gray')
    plt.title('g')
    plt.subplot(133)
    plt.imshow(r,cmap='gray')
    plt.title('r')

    plt.show()     

def bgrChannelColor(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    b,g,r = cv.split(img) 
    zeros = np.zeros_like(b)
    bImg = cv.merge((b,zeros,zeros))
    gImg = cv.merge((zeros,g,zeros))
    rImg = cv.merge((zeros,zeros,r))

    plt.figure() 
    plt.subplot(131)
    plt.imshow(bImg)
    plt.subplot(132)
    plt.imshow(gImg)
    plt.subplot(133)
    plt.imshow(rImg)
    plt.show() 


if __name__ == '__main__': 
    # pureColors() 
    # bgrChannelGrayscale()
    bgrChannelColor() 