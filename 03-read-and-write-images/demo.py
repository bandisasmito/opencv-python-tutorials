import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def readImage(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow('img',img)
    cv.waitKey(0)

def writeImage(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    outPath = os.path.join(root,'demoImages\\output.jpg')
    cv.imwrite(outPath,img)

if __name__ == '__main__': 
    readImage()
    # writeImage()