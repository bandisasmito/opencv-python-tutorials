import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

def contours(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)
    img = img[2680:2860,1490:1720]

    plt.figure() 
    plt.subplot(231)
    plt.imshow(img,cmap='gray')

    height,width = img.shape
    scale = 4 
    heightScale = int(scale*height)
    widthScale = int(scale*width)
    img = cv.resize(img,(widthScale,heightScale))

    _,thresh = cv.threshold(img,65,255,cv.THRESH_BINARY)
    kernel = np.ones((7,7),np.uint8)
    thresh = cv.dilate(thresh,kernel)
    contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    contours = [contours[0]]
    cv.drawContours(img,contours,-1,(0,0,255),3)

    plt.subplot(232)
    plt.imshow(thresh,cmap='gray')
    plt.subplot(233)
    plt.imshow(img,cmap='gray')

    M = cv.moments(contours[0])
    Cx = int(M['m10']/M['m00'])
    Cy = int(M['m01']/M['m00'])

    plt.subplot(234)
    plt.imshow(img,cmap='gray')
    plt.plot(Cx,Cy,'r*')

    area = cv.contourArea(contours[0])
    perimeter = cv.arcLength(contours[0],True)

    epsilon = .01*perimeter
    approx = cv.approxPolyDP(contours[0],epsilon,True)
    approx = np.array(approx)
    approx = np.concatenate((approx,approx[:1]),axis=0)
    plt.plot(approx[:,0,0],approx[:,0,1])

    hull = cv.convexHull(contours[0])
    hull = hull[:,0,:]
    hull = np.concatenate((hull,hull[:1]),axis=0)
    plt.subplot(235)
    plt.imshow(img,cmap='gray')
    plt.plot(hull[:,0],hull[:,1],'r-')

    x,y,w,h = cv.boundingRect(contours[0])
    plt.subplot(236)
    cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    plt.imshow(img,cmap='gray')
    plt.show() 

    aspectRatio = w/h 
    extent = area(w*h)
    solidity = area/cv.contourArea(hull)
    equiDIa = np.sqrt(4*area/np.pi)
    _,_,_angle = cv.fitEllipse(contours[0])

if __name__ == '__main__': 
    contours() 