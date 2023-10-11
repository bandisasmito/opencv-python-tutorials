import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def readImage(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    # imgPath = os.path.join(root,'demoImages\\opencv.png')

    '''
        cv.imread(fileName)
            reads in the image 

        @param fileName
            str, name of the file/path
        @returns 
            ndarry,    
            uint8 (2^8 = 256 or 0-255)

            EX: 985 x 1170 x 3 (rgb channels)
    '''
    img = cv.imread(imgPath)

    # break to see 
    debug = 1 

    '''
        cv.imshow(winname,mat) 
            plots the image

        @param winname 
            str, Name of the window.
        @param mat 
            ndarry, Image to be shown. (mxnx3) or (mxnx1)
    '''
    cv.imshow("img",img)

    '''
        cv.waitKey(delay)
            when you click any key, the image will close 

        @param delay 
            int, Delay in milliseconds. 
            0 is the special value that means "forever"
    '''
    cv.waitKey(0)
    '''
        Split the image into color channels
    '''

def writeImage(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    outPath = os.path.join(root,'demoImages\\output.jpg')
    cv.imwrite(outPath,img)

if __name__ == '__main__': 
    readImage() 
    # writeImage() 
