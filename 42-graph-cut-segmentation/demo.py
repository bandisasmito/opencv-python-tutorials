import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 
import os 

def graphCutSeg(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure()
    plt.subplot(231)
    plt.imshow(img)

    plt.subplot(232)
    rows,cols,_ = img.shape
    mask = np.zeros((rows,cols),np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    x0 = 360 
    y0 = 1470
    x1 = 2800
    y1 = 3700
    rect = (x0,y0,x1-x0,y1-y0)
    iter = 1 
    cv.grabCut(img,mask,rect,bgdModel,fgdModel,iter,cv.GC_INIT_WITH_RECT)
    plt.imshow(mask)

    plt.subplot(233)
    maskGC = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    imgSeg = img*maskGC[:,:,np.newaxis]
    plt.imshow(imgSeg)

    plt.subplot(234)
    maskPath = os.path.join(root,'demoImages//tesla_graphcut.jpg')
    markedMask = cv.imread(maskPath,cv.IMREAD_GRAYSCALE)
    mask[markedMask==255] = 1 
    cv.grabCut(img,mask,None,bgdModel,fgdModel,iter,cv.GC_INIT_WITH_MASK)
    plt.imshow(mask)

    plt.subplot(235)
    maskGC = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    imgSeg = img*maskGC[:,:,np.newaxis]
    plt.imshow(imgSeg)

    plt.show() 

if __name__ == '__main__': 
    graphCutSeg() 