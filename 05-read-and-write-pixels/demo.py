import cv2 as cv 
import os 
import matplotlib.pyplot as plt

def readAndWriteSinglePixel(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    eyePixel = imgRGB[312,350]
    imgRGB[312,350] = (255,0,0)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 
    debug = 1

def readAndWritePixelRegion(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    eyeRegion = imgRGB[290:340,326:380]

    dx = 340-290
    dy = 380-326

    startX = 238 
    startY = 411 

    imgRGB[startX:startX+dx, startY:startY+dy] = eyeRegion
    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 
    debug =1 


if __name__ == '__main__': 
    # readAndWriteSinglePixel() 
    readAndWritePixelRegion()