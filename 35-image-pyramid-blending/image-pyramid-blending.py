import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


def imagePyramidBlending(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    imgBGR = cv.imread(imgPath)
    imgRGB = cv.cvtColor(imgBGR,cv.COLOR_BGR2RGB)
 
    # Get Gaus Pyramid for BGR
    plt.figure() 
    downSamp = imgBGR.copy()
    BGR_gausPyramidList = [downSamp] 
    plt.subplot(2,3,1)
    plt.imshow(downSamp)
    for i in range(5):
        plt.subplot(2,3,i+2)
        downSamp = cv.pyrDown(downSamp)
        plt.imshow(downSamp)
        BGR_gausPyramidList.append(downSamp)

    # Get Laplacian Pyramid for BGR
    plt.figure() 
    BGR_lapPyramidList = [BGR_gausPyramidList[4]] 

    for i in range(4,0,-1): 
        plt.subplot(2,3,4-i+1)
        upSamp = cv.pyrUp(BGR_gausPyramidList[i])
        diff = cv.subtract(BGR_gausPyramidList[i-1],upSamp)
        BGR_lapPyramidList.append(diff)
        plt.imshow(diff)

    # Get Gaus Pyramid for RGB
    plt.figure() 
    downSamp = imgRGB.copy()
    RGB_gausPyramidList = [downSamp] 
    plt.subplot(2,3,1)
    plt.imshow(downSamp)
    for i in range(5):
        plt.subplot(2,3,i+2)
        downSamp = cv.pyrDown(downSamp)
        plt.imshow(downSamp)
        RGB_gausPyramidList.append(downSamp)

    # Get Laplacian Pyramid for RGB
    plt.figure() 
    RGB_lapPyramidList = [RGB_gausPyramidList[4]] 
    for i in range(4,0,-1): 
        plt.subplot(2,3,4-i+1)
        upSamp = cv.pyrUp(RGB_gausPyramidList[i])
        diff = cv.subtract(RGB_gausPyramidList[i-1],upSamp)
        RGB_lapPyramidList.append(diff)
        plt.imshow(diff)

    # Now add left and right halves of images in each level
    combinedList = []
    plt.figure() 
    offset = 7
    for i in range(len(RGB_lapPyramidList)): 
        left = RGB_lapPyramidList[i]
        right = BGR_lapPyramidList[i]
        _,cols,_ = left.shape
        combined = np.hstack((left[:,0:cols//2+offset], right[:,cols//2+offset:]))
        combinedList.append(combined)
        plt.subplot(2,3,i+1)
        plt.imshow(combined)

    # now reconstruct
    blend = combinedList[0] # colored image 
    for i in range(1,4):
        blend = cv.pyrUp(blend)
        blend = cv.add(blend, combinedList[i])

    plt.figure() 
    plt.imshow(blend)
    plt.show() 

if __name__ == '__main__': 
    imagePyramidBlending() 