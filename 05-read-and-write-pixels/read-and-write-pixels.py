import cv2 as cv 
import os 
import matplotlib.pyplot as plt 

def readAndWriteSinglePixel(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    # Read pixel value 
    # imgRGB[row-y,col-x]
    eyePixel = imgRGB[312,350]

    # Write pixel value 
    imgRGB[312,350] = (255,0,0)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 
    debug = 1 


    
def readAndWritePixelRegion(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    eyeRegion = imgRGB[290:340,326:380]
    dx = 340-290
    dy = 380-326

    debug = 1 

    startX = 238 
    startY = 411
    imgRGB[startX:startX+dx,startY:startY+dy] = eyeRegion

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 


if __name__ == '__main__': 
    # readAndWriteSinglePixel() 
    readAndWritePixelRegion()