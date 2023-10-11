import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy 
import os 


def histBackproj(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    # Original Image
    plt.figure() 
    plt.subplot(231)
    plt.imshow(img)

    # Region 
    imgRegion = img[2200:2700,1000:1500,:]
    plt.subplot(232)
    plt.imshow(imgRegion)

    # Backproject to extract part of image similar to region 
    imgRegionHSV = cv.cvtColor(imgRegion,cv.COLOR_RGB2HSV)
    imgRegionHist = cv.calcHist([imgRegionHSV],[0,1],None,[180,256],[0,180,0,256])
    cv.normalize(imgRegionHist,imgRegionHist,0,255,cv.NORM_MINMAX)
    imgHSV = cv.cvtColor(img,cv.COLOR_RGB2HSV)
    out = cv.calcBackProject([imgHSV],[0,1],imgRegionHist,[0,180,0,256],1)
    plt.subplot(233)
    plt.imshow(out)

    # Join regions 
    ellipseKernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(15,15))
    cv.filter2D(out,-1,ellipseKernel,out)
    plt.subplot(234)
    plt.imshow(out)
    
    # Create mask 
    _,mask = cv.threshold(out,70,255,0)
    plt.subplot(235)
    plt.imshow(mask)

    # Apply mask to image 
    maskAllChannels = cv.merge((mask,mask,mask))
    imgSeg = cv.bitwise_and(img,maskAllChannels)
    plt.subplot(235)
    plt.imshow(imgSeg)
    
    plt.show() 


if __name__ == '__main__': 
    histBackproj() 
