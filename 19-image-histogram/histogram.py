import cv2 as cv 
import numpy as np 
import os 
import matplotlib.pyplot as plt 


def grayHistogram(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img,cmap='gray')
    
    '''
        cv.calcHist(image,channels,mask,histSize,histRange - computes the histogram
            @param image List of ndarray 
            @param channels List of channel 
            @param mask Numpy array 
            @param histSize List of number of bins used 
            @param histRange List range of values 
    '''
    # 0 inclusive, 256 exclusive
    hist = cv.calcHist([img], [0], None, [256], [0, 256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel("bins")
    plt.ylabel("# of pixels")
    plt.show()

def colorHistogram(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)

    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    
    colors = ['b','g','r']

    plt.figure()
    for i in range(len(colors)): 
        hist = cv.calcHist([imgRGB], [i], None, [256], [0, 256])
        plt.plot(hist,colors[i])
    plt.xlabel("pixel intensity")
    plt.ylabel("# of Pixels")
    plt.show()

def histogramOfRegion(): 
    '''
        you can use mask, but i prefer to just get the region of the image 
    '''
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)

    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(imgRGB)

    # NEW CODE HERE (rest the same as previous function)
    # imgRGB = imgRGB[286:345,322:389,:]
    imgRGB = imgRGB[675:825,600:800,:]

    plt.figure()
    plt.imshow(imgRGB)
    
    colors = ['b','g','r']

    plt.figure()
    for i in range(len(colors)): 
        hist = cv.calcHist([imgRGB], [i], None, [256], [0, 256])
        plt.plot(hist,colors[i])
    plt.xlabel("pixel intensity")
    plt.ylabel("# of pixels")
    plt.show()

if __name__ == '__main__': 
    # grayHistogram() 
    colorHistogram()
    # histogramOfRegion() 