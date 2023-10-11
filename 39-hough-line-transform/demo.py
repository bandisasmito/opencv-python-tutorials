import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 
import os 


def houghLineTransform(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)
    imgBlur = cv.GaussianBlur(img,(21,21),3)
    cannyEdge = cv.Canny(imgBlur,50,180)

    plt.figure() 
    plt.subplot(141)
    plt.imshow(img)
    plt.subplot(142)
    plt.imshow(imgBlur)
    plt.subplot(143)
    plt.imshow(cannyEdge)

    distResol = 1 
    angleResol = np.pi/180
    threshold = 150 
    lines = cv.HoughLines(cannyEdge,distResol,angleResol,threshold)

    k = 3000 

    for curLine in lines: 
        rho,theta = curLine[0]
        dhat = np.array([[np.cos(theta)],[np.sin(theta)]])
        d = rho*dhat 
        lhat = np.array([[-np.sin(theta)],[np.cos(theta)]])
        p1 = d + k*lhat
        p2 = d - k*lhat
        p1 = p1.astype(int)
        p2 = p2.astype(int)
        cv.line(img,(p1[0][0],p1[1][0]),(p2[0][0],p2[1][0]),(255,255,255),10)


    plt.subplot(144)
    plt.imshow(img)
    
    plt.show() 

if __name__ == '__main__': 
    houghLineTransform() 