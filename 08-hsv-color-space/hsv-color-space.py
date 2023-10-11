import cv2 as cv 
import os 
import numpy as np 
import matplotlib.pyplot as plt 

'''
Good site to understand hsv: 
    OPEN IN INCOGNITO WINDOW (SECURITY REASONS)
    https://web.cs.uni-paderborn.de/cgvb/colormaster/web/color-systems/hsv.html

Formula: 
    https://math.stackexchange.com/questions/556341/rgb-to-hsv-color-conversion-algorithm


OpenCV Application: 
    https://www.educba.com/opencv-hsv-range/


'''
def hsvColorSegmentation(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    '''

    
        hsv ranges 
            h - 0 to 180 (standard is 360)
            s - 0 to 255 (sometimes will see 0 to 1)
            v - 0 to 255 
    '''
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    '''
        can change range of V from 0 - 100 to 50-100
        to get less dark areas to better capture the nose 
        and ears and less of the hair 
    '''
    # lowerBound = np.array([0,0,0])
    lowerBound = np.array([0,0,50])
    upperBound = np.array([10,120,100])
    mask = cv.inRange(hsv,lowerBound,upperBound)
    cv.inRange

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    # cv.waitKey(0)

    cv.imshow('mask',mask)
    cv.waitKey(0) 




if __name__ == '__main__': 
    hsvColorSegmentation() 


