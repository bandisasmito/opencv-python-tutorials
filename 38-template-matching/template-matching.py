import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy 
import os 


def templateMatching(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    telsaLogo = img[2680:2860,1490:1720]
    height,width,_ = telsaLogo.shape

    plt.figure()
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(telsaLogo)

    methods = [cv.TM_CCOEFF,
               cv.TM_CCOEFF_NORMED,
               cv.TM_CCORR,
               cv.TM_CCORR_NORMED,
               cv.TM_SQDIFF,
               cv.TM_SQDIFF_NORMED]
    
    titles = ['cv.TM_CCOEFF',
              'cv.TM_CCOEFF_NORMED',
              'cv.TM_CCORR',
              'cv.TM_CCORR_NORMED',
              'cv.TM_SQDIFF',
              'cv.TM_SQDIFF_NORMED']
  
    for i in range(len(methods)): 
        curImg = img.copy() # bc we are drawing on the image with cv.rectangle
        templateMap = cv.matchTemplate(img,telsaLogo,methods[i])
        _,_,minLoc,maxLoc = cv.minMaxLoc(templateMap)

        if methods[i] == cv.TM_SQDIFF or methods[i] == cv.TM_SQDIFF_NORMED: 
            topLeft = minLoc
        else: 
            topLeft = maxLoc

        bottomRight = (topLeft[0]+width,topLeft[1]+height)
        cv.rectangle(curImg,topLeft,bottomRight,(255,255,255),10)
        plt.figure() 
        plt.subplot(121)
        plt.imshow(templateMap)
        plt.title(titles[i])
        plt.subplot(122)
        plt.imshow(curImg)
 
    plt.show() 

if __name__ == '__main__': 
    templateMatching() 