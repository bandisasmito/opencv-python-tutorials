import os 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def rotation():
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    height,width,_ = img.shape
    '''
        cv.getRotationMatrix2D(dim,angle,scale)
            @param dim Tuple output dim
            @param angle Float angle of rotation in deg 
            @param scale Float scale factor 
            @return 2x3 transformation matrix 
    '''
    T = cv.getRotationMatrix2D((width/2,height/2),180,1)
    imgTrans = cv.warpAffine(img,T,(width,height))
    cv.imshow('imgTrans',imgTrans)
    cv.waitKey(0)

    debug = 1 

if __name__ == '__main__': 
    rotation() 
